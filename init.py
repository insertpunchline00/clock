import colorsys
import signal
import time
import datetime
from datetime import date, timedelta
from darksky import forecast
from sys import exit
import Displays
import weather_call

import unicornhathd

print("""Version0.1""")

#colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x/float(len(lines)), 1.0, 1.0)]) for x in range(len(lines))]


now = datetime.datetime.now()
hour = datetime.datetime.now().strftime("%H")
minute = datetime.datetime.now().strftime("%M")
weekday = date.today()

temperature, weather_symbol=weather_call.weather_now(49.7685,9.9382)

print(weather_symbol)
print (temperature)

#temperature="12" #for tests
Displays.display_clock(hour,minute,temperature,weather_symbol,1.0)

#Displays.display_image('Lama.png',1)

unicornhathd.show()


