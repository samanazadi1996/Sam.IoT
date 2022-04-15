import RPi.GPIO as GPIO
import time

pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
on = True

try:
    print('Blinking LED. Press Ctrl+C to end.')
    while True:
        time.sleep(1)
        GPIO.output(pin, int(on))
        on = not on
finally:
    GPIO.cleanup()
