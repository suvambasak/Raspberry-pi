import picamera

camera = picamera.PiCamera()
camera.capture('example.jpg')

camera.vflip = True

camera.capture('example2.jpg')