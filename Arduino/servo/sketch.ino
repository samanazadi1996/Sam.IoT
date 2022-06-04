#include <Servo.h>

Servo myservo;
const int servopin = 9;

void setup()
{
	myservo.attach(servopin);
}
void loop()
{
	myservo.write(random(0, 180));
  delay(2000);
}
