import RPi.GPIO as GPIO

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(2)

try:
  while True:
    i = int(input("enter number betwen 0 to 12 >>> "))
    p.ChangeDutyCycle(i)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()