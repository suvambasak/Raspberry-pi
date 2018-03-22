import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

try:
    while True:
        print ("LED ON")
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
        
        print ("LED OFF")
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.5)
finally:
    GPIO.cleanup()
