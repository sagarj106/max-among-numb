import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
 
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    GPIO.output(GPIO_TRIGGER, True)
 
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime

    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
while True:
    dist = distance()
    print ("Measured Distance =",  dist)
    if (dist<50):
        os.system("fswebcam -S 20 -r 1280X720 --no-banner Test2.jpg")
        break
    
GPIO.cleanup()
            