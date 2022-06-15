#include "pitches.h"
#define SPEAKER_PIN 8

void setup()
{
	pinMode(SPEAKER_PIN, OUTPUT);
}
void loop()
{
	tone(SPEAKER_PIN, 1000, 1000);
	delay(2000);
}
