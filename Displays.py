#!/usr/bin/env python

import colorsys
import signal
import time
import datetime
from datetime import date, timedelta
from darksky import forecast
from sys import exit

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhathd





#colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x/float(len(lines)), 1.0, 1.0)]) for x in range(len(lines))]


def display_clock (hours,minutes, temperature, weather_symbol,brightness):  #temperature has tobe  string with at least two chars (add whitspace before)| add color coutner which is counted in main

    FONT = ("/home/pi/.fonts/fixed.ttf", 10) #also time font in file
    FONT2 = ("/home/pi/.fonts/weather.ttf", 6) #font spacing very small! evtl correct with fnt forge


    unicornhathd.rotation(0)
    unicornhathd.brightness(brightness)


    width, height = unicornhathd.get_shape()
    text_x = width
    text_y = 0
    font_file, font_size = FONT
    font_file2, font_size2 = FONT2


    font=ImageFont.truetype(font_file, font_size)
    font2=ImageFont.truetype(font_file2, font_size2)

    w, text_height = font.getsize(hours)

    image = Image.new("RGB", (16,max(16, text_height)), (0,0,0))
    draw = ImageDraw.Draw(image)
    draw.fontmode = "1" #turn antialiasing off for pixel fonts



    draw.line(((11,0),(11,15)),(0,0,255),1)

    draw.text((-1, 1), hours, (255,255,0), font=font)
    draw.text((-1, 9), minutes, (0,255,0), font=font)

    singledigit=0
    if temperature [1]==" ":
        singledigit=6
    
    draw.text((13, 4+singledigit), temperature[0], (0,255,0), font=font2)  #todo whitespace trick refine
    draw.text((13, 10), temperature[1], (0,255,0), font=font2)

    singledigit=0

    for x in range(16):
        for y in range(height):
            pixel = image.getpixel((x, y))
            r, g, b = [int(n) for n in pixel]
            unicornhathd.set_pixel(-x-1, y, r, g, b)

    img = Image.open(weather_symbol+'.png')#display weather icon , image name == returned status from api
         
    for o_x in range(img.size[0]):
     for o_y in range(img.size[1]):                
        pixel = img.getpixel((o_x,o_y))
        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])           
        unicornhathd.set_pixel(o_x, o_y, r, g, b)

    unicornhathd.show()
   
    return



def display_image(image, brightness):
    unicornhathd.rotation(0)
    unicornhathd.brightness(brightness)

    width, height = unicornhathd.get_shape()
    img = Image.open(image)

    for x in range(width):
        for y in range(height):

            pixel = img.getpixel((x, y))
            r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                        
            unicornhathd.set_pixel(x, y, r, g, b)
                   
    unicornhathd.show()
    time.sleep(1)

    

    return


def display_animation(image, brightness):#displays a animation as multi png
    unicornhathd.rotation(90)
    unicornhathd.brightness(brightness)

    width, height = unicornhathd.get_shape()
    img = Image.open(image)

    try:
        while True:
            for o_x in range(int(img.size[0]/width)):
                for o_y in range(int(img.size[1]/height)):

                    valid = False
                    for x in range(width):
                        for y in range(height):
                            pixel = img.getpixel(((o_x*width)+y,(o_y*height)+x))
                            r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                            if r or g or b:
                                valid = True
                            unicornhathd.set_pixel(x, y, r, g, b)
                    if valid:
                        unicornhathd.show()
                        time.sleep(1)

    except KeyboardInterrupt:
        unicornhathd.off()
    return


   

##def display_timetable (times_magirus,times_koenigs,brightness):  #temperature has tobe  string with at least two chars (add whitspace before)| add color coutner which is counted in main
##
##    
##    FONT = ("/home/pi/.fonts/weather.ttf", 6) #font spacing very small! evtl correct with fnt forge
##
##
##    unicornhathd.rotation(0)
##    unicornhathd.brightness(brightness)
##
##
##    width, height = unicornhathd.get_shape()
##    text_x = width
##    text_y = 0
##   
##    font_file, font_size = FONT
##
##
##    
##    font=ImageFont.truetype(font_file, font_size)
##
##    w, text_height = font.getsize(times_magirus[1])
##
##    image = Image.new("RGB", (16,max(16, text_height)), (0,0,0))
##    draw = ImageDraw.Draw(image)
##    draw.fontmode = "1" #turn antialiasing off for pixel fonts
##
##
##
##    draw.line(((11,0),(11,15)),(0,0,255),1)
##
##    draw.text((-1, 1), str(times_magirus[1]), (255,255,0), font=font)
##    draw.text((-1, 9), minutes, (0,255,0), font=font)
##
##    draw.text((13, 4), temperature[0], (0,255,0), font=font2)  #todo whitespace trick refine
##    draw.text((13, 10), temperature[1], (0,255,0), font=font2)
##
##    for x in range(16):
##        for y in range(height):
##            pixel = image.getpixel((x, y))
##            r, g, b = [int(n) for n in pixel]
##            unicornhathd.set_pixel(-x-1, y, r, g, b)
##
##    
##
##    unicornhathd.show()
##   
##    return




   

