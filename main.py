import machine
import time
from bme680 import BME680
from io_pubsub import IOClient

adc = machine.ADC(machine.Pin(35))
adc.atten(machine.ADC.ATTN_11DB)  # provides full range of 0-4095

led = machine.Pin(22, machine.Pin.OUT)  # LED on the board
led.value(0)
bme680 = BME680()
io = IOClient()

while True:
    battery = (adc.read() * 2 * 3.3) / 4096
    print("Battery: %d mV", battery)

    io.update(bme680.temperature, bme680.humidity, bme680.pressure, bme680.gas, battery)
    io.publish()
    time.sleep(60)
