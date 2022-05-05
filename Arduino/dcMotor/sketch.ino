#define ENA1 5
#define IN1 8
#define IN2 9

void setup()
{
  pinMode(ENA1, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop()
{
  analogWrite(ENA1, 255);  // Sets speed of motor using PWM 0 - 255
  digitalWrite(IN1, HIGH); // Input 1 is turned on
  digitalWrite(IN2, LOW);  // Input 2 is turned off
}