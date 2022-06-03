from machine import Pin
import utime
import time
import machine

# This file is only made for Raspberry pi pico 

def t(sec):
    time.sleep(sec)

temprature_sensor = machine.ADC(4)
cf = 3.3/(65535)
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
led =  Pin(25, Pin.OUT)

def ultra():
       timepassed=0
       trigger.low()
       utime.sleep_us(2)
       trigger.high()
       utime.sleep_us(5)
       trigger.low()
       while echo.value() == 0:
               sf = utime.ticks_us()
       while echo.value() == 1:
           sn = utime.ticks_us()
       timepassed = sn - sf
       return timepassed

while True:
         measure_time = ultra()
         distance_cm = (measure_time * 0.0343) / 2
         distance_cm = round(distance_cm, 2)
         
         read = temprature_sensor.read_u16()*cf
         temprature = 27 - (read - 0.700)/0.001721
         print(f"Distance: {distance_cm}, Temprature: {temprature}")
         
         if distance_cm < 110:
             led(1)
             speaker = machine.PWM(machine.Pin(7))
             speaker.duty_u16(int(65535/2))
             speaker.freq(500)
         else:
              led(0)
              s = Pin(7, Pin.OUT)
              s(0)

             