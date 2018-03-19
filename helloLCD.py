#!/usr/bin/python
#show IP address on the LCD Plate at startup
#CHoke

import Adafruit_CharLCD as LCD
import time
import subprocess


lcd = LCD.Adafruit_CharLCDPlate()

Name = subprocess.check_output("hostname").strip()
displayText = Name


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


    elif lcd.is_pressed(LCD.UP):
        if wrefresh:
            lcd.clear()
            lcd.set_backlight(1)
            lcd.message("I Like Tacos")
            refresh = True
            wrefresh = False

    elif lcd.is_pressed(LCD.DOWN):
        if wrefresh:
            lcd.clear()
            lcd.set_backlight(1)
            lcd.message("Do You Like" + "\n" "Tacos?")
            refresh = True
            wrefresh = False

    elif lcd.is_pressed(LCD.LEFT):
        if wrefresh:
            lcd.clear()
            lcd.set_backlight(1)
            lcd.message("Yes?" + "\n" + "Good!")
            refresh = True
            wrefresh = False

    elif lcd.is_pressed(LCD.RIGHT):
        if wrefresh:
            lcd.clear()
            lcd.set_backlight(1)
            lcd.message("Let's Get'" + "TACOS!")
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








