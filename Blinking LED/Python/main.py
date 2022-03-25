import RPi.GPIO as GPIO
import time

pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
on = True

while True:
    print(f'led {on}')
    time.sleep(1)
    GPIO.output(pin, int(on))
    on = not on
