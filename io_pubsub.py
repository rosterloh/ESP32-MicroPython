import network
import time
import machine
import ubinascii
import credentials
from umqtt.simple import MQTTClient

class IOClient:

    def __init__(self):
        self._client = ubinascii.hexlify(machine.unique_id())
        self._feed = credentials.adafruitUsername + "/feeds/"
        self._url = "io.adafruit.com"
        self._sta_if = network.WLAN(network.STA_IF)
        self._io = MQTTClient(self._client, self._url, 0, credentials.adafruitUsername, credentials.adafruitAioKey)
        self._data = dict([('temperature', 0), ('humidity', 0), ('pressure', 0), ('gas', 0), ('battery', 0)])

    def publish(self):
        if not self._sta_if.isconnected():
            self._sta_if.active(True)
            self._sta_if.connect(credentials.wifiSsid, credentials.wifiPassword)
            while not self._sta_if.isconnected():
                pass

        self._io.connect()
        for k, v in self._data.items():
            feed = self._feed + k
            self._io.publish(feed, str(v))

        self._io.check_msg()
        self._io.disconnect()
        self._sta_if.disconnect()
        self._sta_if.active(False)

    def update(self, t, h, p, g, b):
        self._data['temperature'] = t
        self._data['humidity'] = h
        self._data['pressure'] = p
        self._data['gas'] = g
        self._data['battery'] = b
