#!/usr/bin/python
#show IP address on the LCD Plate at startup
#CHoke

import Adafruit_CharLCD as LCD
import time
import subprocess
  # lint:ok

lcd = LCD.Adafruit_CharLCDPlate()

Name = subprocess.check_output("hostname").strip()
displayText = Name
  # lint:ok

IP = subprocess.check_output(["hostname", "-I"])

lcd.clear()
lcd.message("displayText\n")

while(True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message("displayText\n")
        lcd.set_backlight(1)
        lcd.message("Hello World\n")
        time.sleep(0.5)
    else:
        lcd.set_backlight(1)
        lcd.message(displayText)
        lcd.message(IP)
        time.sleep(0.5)
        lcd.clear()


