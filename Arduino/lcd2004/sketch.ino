#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);

void setup()
{
  lcd.init();
  lcd.backlight();
}

void loop()
{
  // lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Hello Arduino");
}