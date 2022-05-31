import machine
from machine import Pin

# This code is only made for Raspberry pi pico

led = Pin(25, Pin.OUT)

temperature_sensor = machine.ADC(4)
cf = 3.3/(65535)

while True:
    read = temperature_sensor.read_u16()*cf
    temperature = 27 - (read - 0.700)/0.001721
    print(temperature)

    if temperature > 30:
         led(1)
    else:
         led(0)