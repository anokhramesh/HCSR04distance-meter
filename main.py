from machine import I2C,Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime
import time
trigger =Pin(3,Pin.OUT)
echo =Pin(2,Pin.IN)
i2c=I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
lcd=I2cLcd(i2c,0x27,2,16)
lcd.move_to(0,0)
lcd.putstr("Anokh Automation")
lcd.move_to(0,1)
lcd.putstr("Please Subscribe")
time.sleep(2)
lcd.clear()

while True:
    trigger.value(0)
    utime.sleep_us(2)
    trigger.value(1)
    utime.sleep_us(5)
    trigger.value(0)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon=utime.ticks_us()
    timepassed=signalon-signaloff
    distance = (timepassed *0.0343)/2
    print("The distance",distance,"cm")
    lcd.move_to(0,0)
    lcd.putstr("Distance meter")
    lcd.move_to(0,1)
    lcd.putstr(str(distance)+"cm")
    utime.sleep(1)