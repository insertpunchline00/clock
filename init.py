import colorsys
import signal
import time
import datetime
from datetime import date, timedelta
from darksky import forecast
from sys import exit
import Displays
import weather_call
import random
import unicornhathd

print("""Version0.1""")
#default weather symbol,temperature
#colorcycle_clock=random.randint(0, 16)
#colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x/float(len(lines)), 1.0, 1.0)]) for x in range(len(lines))]
update_weather=0
temperature, weather_symbol=weather_call.weather_now(49.7685,9.9382)
minute_old=0

while True:
    now = datetime.datetime.now()
    hour = datetime.datetime.now().strftime("%H")
    minute = datetime.datetime.now().strftime("%M")
    weekday = date.today()
    
    if (minute!=minute_old):
        colorcycle_clock=random.randint(0, 16)
    minute_old=minute
    if update_weather >120:
        
        try:
            temperature, weather_symbol=weather_call.weather_now(49.7685,9.9382)
            print("weather_updated")

        except error101:
            continue
        update_weather=0

    print (update_weather)
    print(weather_symbol)
    print (temperature)

    #temperature="50  " #for tests

        
    Displays.display_clock(hour,minute,1.0,colorcycle_clock,16) #hour
    Displays.display_temperature(temperature,weather_symbol,1.0)




    # Displays.display_image('Lama.png',1)
    update_weather +=1
    unicornhathd.show()
    #unicornhathd.off()
    time.sleep(1)
