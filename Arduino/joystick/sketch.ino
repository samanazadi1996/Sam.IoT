#define joyX A0
#define joyY A1

void setup()
{
  Serial.begin(9600);
}
void loop()
{
  int xValue = analogRead(joyX);
  int yValue = analogRead(joyY);
}
