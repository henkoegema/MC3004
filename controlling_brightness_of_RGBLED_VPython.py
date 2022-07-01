#!/usr/bin/python3

from gpiozero import PWMLED, MCP3004
from time import sleep
import RPi.GPIO as GPIO
from vpython import *


potRed = MCP3004(0)
potGreen = MCP3004(1)
potBlue = MCP3004(2)

ledRed = PWMLED(18)
ledGreen =PWMLED(14)
ledBlue = PWMLED(15)

mySphere = sphere(color = color.white, radius = 1, pos =vector(0,2.5,0))
myCyl = cylinder(color = color.white, radius =1, length = 2.5, axis = vector(0,1,0))
myBase = cylinder(color = color.white, radius =1.2, length = 0.25, axis = vector(0,1,0))
myLeg1 = box(pos = vector(-0.75,-3,0),size = vector(0.1,6,0.1), color = vector(0.2,0.2,0.2))
myLeg2 = box(pos = vector(-0.25,-3,0),size = vector(0.1,6,0.1), color = vector(0.2,0.2,0.2))
myLeg3 = box(pos = vector(0.25,-3,0),size = vector(0.1,6,0.1), color = vector(0.2,0.2,0.2))
myLeg4 = box(pos = vector(0.75,-3,0),size = vector(0.1,6,0.1), color = vector(0.2,0.2,0.2))

try:
    while True:
       rate = (20) 
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
        #print(potGreen.value)
        sleep(0.1)
        
       if (potBlue.value < 0.02):
         ledBlue.value = 0
       else:
        ledBlue.value = potBlue.value
        #print(potBlue.value)
        sleep(0.1)
        
             
       mySphere.color = vector(ledRed.value,ledGreen.value,ledBlue.value)
       myCyl.color = vector(ledRed.value,ledGreen.value,ledBlue.value)
       myBase.color = vector(ledRed.value,ledGreen.value,ledBlue.value)
       #sleep(0.5)      
        

except KeyboardInterrupt:
    GPIO.cleanup()
    print()
    print('GPIO cleaned up')
