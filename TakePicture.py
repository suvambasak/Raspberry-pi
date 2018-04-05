import picamera
import os

camera = picamera.PiCamera()
camera.capture('example.jpg')

if not os.path.exists('flip'):
	os.makedirs('flip')

camera.vflip = True

camera.capture('flip/example2.jpg')
