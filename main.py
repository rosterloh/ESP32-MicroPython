import machine
import time
from bme680 import BME680

adc = machine.ADC(machine.Pin(35))
adc.atten(machine.ADC.ATTN_11DB)  # provides full range of 0-4095

led = machine.Pin(22, machine.Pin.OUT)  # LED on the board
bme680 = BME680()

while True:
    #if adc.read() > 2048:
    #    led.value(1)
    #else:
    #    led.value(0)
    #time.sleep_ms(20)
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)

    time.sleep(2)
