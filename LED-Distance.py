import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18
LED = 23

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(LED, GPIO.OUT)


try:
    while True:
        time.sleep(1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == False:
            start = time.time()
        
        while GPIO.input(ECHO) == True:
            end = time.time()
        
        sig_time = end-start

        #cm:
        distance = sig_time / 0.000058
        
        if distance < 100:
            GPIO.output(LED, True)
        else:
            GPIO.output(LED, False)

        #inches:
        #distance = sig_time / 0.000148

        print ('Distance : {} cm'.format(distance))

finally:
    GPIO.cleanup()

