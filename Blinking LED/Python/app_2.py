import RPi.GPIO as GPIO
import time

pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

step = 10
light = 10

p = GPIO.PWM(pin, 100)
p.start(light)

try:
    while True:
        if light in [0, 100]:
            step *= -1
        light += step
        p.ChangeDutyCycle(light)
        time.sleep(1)
finally:
    p.stop()
    GPIO.cleanup()
