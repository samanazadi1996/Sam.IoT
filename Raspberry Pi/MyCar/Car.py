import RPi.GPIO as GPIO

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(2)

def ChangeDutyCycle(x):
    p.ChangeDutyCycle(x)
