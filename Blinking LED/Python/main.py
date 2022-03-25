import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

on = True

while True:
    print(f'led {on}')
    time.sleep(1)
    GPIO.output(4, int(on))
    on = not on
