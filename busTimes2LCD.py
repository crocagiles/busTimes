import time
import os
##os.chdir('/home/pi/Desktop/GreenHouseBusTimes/')
import Adafruit_CharLCD as LCD
from greenHouseBusTimes import *
import random

time.sleep(5)

lcd_rs        = 27
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
                           lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()


while True:
    busTimes = greenHouseBusTimes()
    #for i in range(len(busTimes)):
    for bus in busTimes:
        for minutes in bus:
            print(minutes)
        
    lcd.clear()
    #lcd.message(busTimes[i][0] + '\n' + busTimes[i][1])
    time.sleep(4)
    rand = 1#random.randrange(1, 20)

    
    if rand == 1:
        lcd.clear()
        lcd.message("Zach == 'Nerd'")
        lcd.show_cursor(True)
        lcd.blink(True)
        time.sleep(1.5)
        lcd.show_cursor(False)
        lcd.blink(False)
        lcd.clear()
        lcd.message("Zach == 'Nerd'\nTRUE")
        time.sleep(0.6)
        lcd.clear()
        lcd.message("Zach == 'Nerd'\nTRUE lol")
        time.sleep(0.1)
        
