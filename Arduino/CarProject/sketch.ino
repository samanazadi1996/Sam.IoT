#include <Servo.h>

Servo myservo;
#define joyX A0
#define joyY A1

const int servopin = 9;
const int ledpin = 7;
const int dirPin = 2;
const int stepPin = 3;

void setup()
{
	myservo.attach(servopin);
	Serial.begin(9600);
	pinMode(stepPin, OUTPUT);
	pinMode(dirPin, OUTPUT);
	pinMode(ledpin, OUTPUT);
}
void loop()
{
	int xValue = analogRead(joyX);
	int yValue = analogRead(joyY);

	if (yValue != 512)
	{
		digitalWrite(dirPin, yValue > 512);
		digitalWrite(stepPin, HIGH);
		delayMicroseconds(100);
		digitalWrite(stepPin, LOW);
		delayMicroseconds(100);
	}
	digitalWrite(ledpin, yValue == 512);

	myservo.write(map(xValue, 0, 1023, 0, 180));
}
