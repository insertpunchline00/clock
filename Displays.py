#!/usr/bin/env python

import colorsys
import signal
import time
import datetime
import random
from datetime import date, timedelta
from darksky import forecast
from sys import exit

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhathd





#colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x/float(len(lines)), 1.0, 1.0)]) for x in range(len(lines))]


def display_clock (hours,minutes,brightness,cycle,color_width):  #temperature has tobe  string with at least two chars (add whitspace before)| add color coutner which is counted in main

    FONT = ("/home/pi/.fonts/fixed.ttf", 10) #also time font in file
    


    unicornhathd.rotation(0)
    unicornhathd.brightness(brightness)


    width, height = unicornhathd.get_shape()
    text_x = width
    text_y = 0
    font_file, font_size = FONT
    
    font=ImageFont.truetype(font_file, font_size)
 

    w, text_height = font.getsize(hours)

    image = Image.new("RGB", (16,max(16, text_height)), (0,0,0))
    draw = ImageDraw.Draw(image)
    draw.fontmode = "1" #turn antialiasing off for pixel fonts


    #draw.line(((11,0),(11,15)),(0,0,255),1)

    #draw.text((-1, 1), hours, (255,255,0), font=font)
    #todo change rand int colours
    draw.text((-1, 0), hours, ( 0, 255, 0), font=font)
    draw.text((-1, 9), minutes, ( 0,255,0), font=font)


    for x in range(12):
        for y in range(16):
            pixel = image.getpixel((x, y))

                       
            r, g, b = [int(n) for n in pixel]
            

            if r>0 or g>0 or b>0:
                
                r, g, b = [int(n * 255) for n in colorsys.hsv_to_rgb((y+cycle) / float(color_width), 1.0, 1.0)]
                

            unicornhathd.set_pixel(-x-1, y, r, g, b)



    #unicornhathd.show()
   
    return

def display_temperature (temperature, weather_symbol,brightness):

    FONT2 = ("/home/pi/.fonts/weather.ttf", 6) #font spacing very small! evtl correct with fnt forge


    font_file2, font_size2 = FONT2

    font2=ImageFont.truetype(font_file2, font_size2)
 

    

    unicornhathd.rotation(0)
    unicornhathd.brightness(brightness)


    width, height = unicornhathd.get_shape()
    text_x = width
    text_y = 0


    w, text_height = font2.getsize(str(temperature))

    image = Image.new("RGB",(16,max(16, text_height)), (0,0,0))
    draw = ImageDraw.Draw(image)
    draw.fontmode = "1" #turn antialiasing off for pixel fonts

    #temperature colorset
    #norm color to -10 +30 degree temperature range
    value=float(30-int(temperature))/40 *0.66
    if value<0:
        value=0
    if value>0.66:
        value=0.66

    rt, gt, bt = [int(n * 255) for n in colorsys.hsv_to_rgb(value, 1.0, 1.0)]
    #end temperature colorset

#digit postion corections for different temperature values e.g. -22 or -6
#standard case is positive two digits

    singledigit=0#correction if just one digit
    doubleminus=0  #if negative and two digits, places first digit
    doubleminus2=0 #if negative and two digits, places second digit
    doubleminus3=0 #if negative and two digits, places minus sign

    if temperature [1]==" ":
        singledigit=6

    if temperature [2]!=" ":
        doubleminus=2
        doubleminus2=6
        doubleminus3=1

  
    draw.text((13-doubleminus, 4+singledigit+doubleminus3), temperature[0], (rt,gt,bt), font=font2)  #whitespace trick refine based on stringlength check todo minus sign
    draw.text((13, 10-doubleminus2), temperature[1], (rt,gt,bt), font=font2)
    draw.text((13, 10), temperature[2], (rt,gt,bt), font=font2)

    singledigit=0
    doubleminus=0
    doublemius2=0
    doubleminus3=0
    
    for x in range(11,16):
        for y in range(16):
            pixel = image.getpixel((x, y))

                       
            r, g, b = [int(n) for n in pixel]
                   
                
            unicornhathd.set_pixel(-x-1, y, r, g, b)
            #print(pixel)



    img = Image.open(weather_symbol+'.png')#display weather icon , image name == returned status from api
         
    for o_x in range(img.size[0]):
     for o_y in range(img.size[1]):                
        pixel = img.getpixel((o_x,o_y))
        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])           
        unicornhathd.set_pixel(o_x, o_y, r, g, b)

    #unicornhathd.show()

    return


def display_image (image, brightness):
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
    #time.sleep(1) #for debug

    

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


   

def display_timetable (times_magirus,times_koenigs,brightness):  #temperature has tobe  string with at least two chars (add whitspace before)| add color coutner which is counted in main

    
    FONT = ("/home/pi/.fonts/weather.ttf", 6) #font spacing very small! evtl correct with fnt forge
    times_magirus=str(times_magirus)
    times_koenigs=str(times_koenigs)

    unicornhathd.rotation(0)
    unicornhathd.brightness(brightness)

    width, height = unicornhathd.get_shape()
    text_x = width
    text_y = 0
   
    font_file, font_size = FONT


    
    font=ImageFont.truetype(font_file, font_size)

    w, text_height = font.getsize("test")

    image = Image.new("RGB", (16,max(16, text_height)), (0,0,0))
    draw = ImageDraw.Draw(image)
    draw.fontmode = "1" #turn antialiasing off for pixel fonts



    
    if len(str(times_magirus))<=1:
        times_magirus=" "+times_magirus

    if len(str(times_koenigs))<=1:
        times_koenigs=" "+times_koenigs

    if len(str(times_magirus))>2:
        times_magirus=" x"+times_magirus

    if len(str(times_koenigs))>2:
        times_koenigs=" x"

    
        
    draw.text((8, 0), str(times_koenigs[0]), (255,0,0), font=font)
    draw.text((12, 0), str(times_koenigs[1]), (255,0,0), font=font)

    draw.text((8, 9), str(times_magirus[0]), (0,255,0), font=font)
    draw.text((12, 9), str(times_magirus[1]), (0,255,0), font=font)
    

    for x in range(16):
        for y in range(height):
            pixel = image.getpixel((x, y))
            r, g, b = [int(n) for n in pixel]
            unicornhathd.set_pixel(-x-1, y, r, g, b)

    imgbus = Image.open("Bus.png")#display busicon
         
    for o_x in range(imgbus.size[0]):
     for o_y in range(imgbus.size[1]):                
        pixel = imgbus.getpixel((o_x,o_y))
        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])           
        unicornhathd.set_pixel(o_x+8, o_y, r, g, b)

    imgbahn = Image.open("Strassenbahn.png")#display tramicon
         
    for o_x in range(imgbahn.size[0]):
     for o_y in range(imgbahn.size[1]):                
        pixel = imgbahn.getpixel((o_x,o_y))
        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])           
        unicornhathd.set_pixel(o_x+8, o_y+9, r, g, b)
    
    

    unicornhathd.show()
   
    return




   

