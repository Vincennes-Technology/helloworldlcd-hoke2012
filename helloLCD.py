#!/usr/bin/python
#show "Hello World on the LCD screen"
#CHoke

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

displayText = "Caleb Loves Pi"

lcd.clear()
lcd.message(displayText)

