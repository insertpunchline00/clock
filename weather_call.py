import colorsys
import signal
import time
import datetime
from datetime import date, timedelta
from darksky import forecast
from sys import exit



 



def weather_now(latitude, longitude):
    temperature="   "
    Location =latitude, longitude    

    with forecast('010f047106b04884f64c9dbb762af52f', *Location,units="si" ) as location:
        temperature=str(int(round(location.temperature)))
        icon=location.icon       

    return  temperature+"  ", icon #whitespaces needed for correct Display
