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
refresh = True
wrefresh = True

while(True):
    if lcd.is_pressed(LCD.SELECT):
        if wrefresh:
            lcd.clear()
            lcd.set_backlight(1)
            lcd.message("Hello World\n")
            refresh = True
            wrefresh = False


    else:
        if refresh:
            lcd.clear()
            lcd.set_backlight(1)
            lcd.message(displayText + "\n")
            lcd.message(IP)
            refresh = False
            wrefresh = True
        time.sleep(0.5)








