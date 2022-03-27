from time import sleep
import RPi.GPIO as GPIO

pins = [7, 11, 12]

GPIO.setmode(GPIO.BOARD)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

index = 0
try:
    while True:
        GPIO.output(int(pins[index]), 0)

        index = 0 if (index == len(pins) - 1) else index + 1

        GPIO.output(int(pins[index]), 1)

        sleep(1)
finally:
    GPIO.cleanup()
