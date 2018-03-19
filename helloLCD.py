#!/usr/bin/python
#show IP address on the LCD Plate at startup
#CHoke

import Adafruit_CharLCD as LCD
import time
import subprocess


lcd = LCD.Adafruit_CharLCDPlate()

displayText = "CalebLikesPi\n"

IP = subprocess.check_output(["hostname", "-I"])

lcd.clear()
lcd.message(displayText)

while(True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message(displayText)
        lcd.set_backlight(1)
        lcd.message(    "Hello World\n")
        time.sleep(2.0)
    else:
        lcd.set_backlight(1)
        lcd.message(displayText)
        lcd.message(IP)
        time.sleep(2.0)
        lcd.clear()


