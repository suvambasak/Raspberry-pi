import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
push = 0
try:
    while True:
        if GPIO.input(11) == True:
            push+=1
            print ("Push :: ",push)
        time.sleep(0.3)
finally:
    GPIO.cleanup()
