#!/usr/bin/python3

from gpiozero import PWMLED, MCP3004
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

potRed = MCP3004(0)
potGreen = MCP3004(1)
potBlue = MCP3004(2)

ledRed = PWMLED(18)
ledGreen =PWMLED(14)
ledBlue = PWMLED(15) 

try:
    while True:
       if (potRed.value < 0.02):
         ledRed.value = 0
       else:
         ledRed.value = potRed.value
         print(potRed.value)
         sleep(0.1)
                
       if (potGreen.value < 0.02):
         ledGreen.value = 0
       else:
         ledGreen.value = potGreen.value
         sleep(0.1)
         
       if (potBlue.value < 0.02):
         ledBlue.value = 0
       else:
         ledBlue.value = potBlue.value
         print(potBlue.value)
         sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print()
    print('GPIO cleaned up')
