#coding: utf-8
"""
###Code Assignment
---Spectral B channel---
Group ID (3bit) [g2g1g0]
Node ID (3bit) [i2i1i0]
Time_1 (10bit(6bit,4bit)) [h5h4h3h2h1h0][m5m4m3m2]

---Spectral G channel---
Time_2 (8bit) [m1m0][s5s4s3s2s1s0]
Temperature (8bit) [a5a4a3a2a1a0]

---Spectra R channel---
Atmospheric Pressure (8bit) [b5b4b3b2b1b0]
Humidity (8bit) [c5c4c3c2c1c0]

###Data Format and Prefixed Values
Encryption Common Key:  10101101
Group ID:  010
Node ID:	000, 001, 010, 011, 100
Time: (0〜23 : 0〜59 : 0〜59)	[h5h4h3h2h1h0][m5m4m3m2m1m0][s5s4s3s2s1s0]
Temperature: (0〜100) [deg]	 [a5a4a3a2a1a0]
Atmospheric pressure: (0〜100)[%][hPa]	 [b5b4b3b2b1b0]
Humidity: (0〜100)[%]	 [c5c4c3c2c1c0]
"""


import cv2
import time
from time import sleep
from datetime import datetime
import numpy as np
import paho.mqtt.subscribe as subscribe
from sense_hat import SenseHat

#myfunction
import Encoder_myfunction

#Myfunc class
myfunc = Encoder_myfunction.MyClass()

#Sensehat class
sense = SenseHat()

#Params---------------------------------------------------------------

#IPaddress
##Mac IP adderss
host = "172.16.120.223"

##子機 IP address
topic1 = "172.16.120.130/lm75b-1/temp"
topic2 = "172.16.120.228/lm75b-1/temp"









#query choice-----------------------------------------------------

msg=subscribe.simple(topic1, hostname=host, retained=False, msg_count=1)
print("msg.topic", msg.topic)
print("get Query")

#------------------------------符号器検出(背景差分)
e=[0,0,0]
w=[255,200,180]
z3 = [e]*64
#z4 = [w]*64
z4 = [
      w,w,w,w,w,w,w,w,
      w,w,w,e,e,w,w,w,
      w,w,e,w,e,w,w,w,
      w,w,w,w,e,w,w,w,
      w,w,w,w,e,w,w,w,
      w,w,w,w,e,w,w,w,
      w,w,e,e,e,e,w,w,
      w,w,w,w,w,w,w,w,
    ]

#1
#点灯
sense.set_pixels(z4)
time.sleep(5)
sense.clear()

#消灯
time.sleep(5)



#Params to be Encoded------------------------------------------------------------------------------------------------

#prefix=01
##This time, Group_ID is static.
Group_ID = [0,1,0]

#Node_ID is varied according to Edge(IoT device)
Node_ID = [0,0,0]

prefix = Group_ID + Node_ID

#time
now = datetime.now()
hour = now.hour
minute = now.minute
second = now.second

###environmental data
#temperature
temperature = sense.get_temperature()
#pressure
#only last 2 digits
pressure = sense.get_pressure() - 1000
#humidity
humidty = sense.get_humidity()

##data_edit-------------------------------------------------------------

###time
hour_binary = myfunc.binary(hour, 6)
minute_binary = myfunc.binary(minute, 6)
second_binary = myfunc.binary(hour, 6)

###environmental data
temper_binary = myfunc.binary(temperature, 8)
press_binary = myfunc.binary(pressure, 8)
humid_binary = myfunc.binary(humidty, 8)

##minute_binary is splited 4bit(Spectral B) and 2bit(Spectral R)
minute_B = minute_binary[0:4:1]
minute_G = minute_binary[4:6:1]

#convert edited data to RGB_array----------------------------------------------------------------------------------------------------
##Spectral B
B_array = prefix + hour_binary + minute_B
##Spectral G
G_array = minute_G + second_binary + temper_binary
##Spectral R
R_array = press_binary + humid_binary

#query choice-----------------------------------------------------

#s1 = list(msg.payload)
query = str(10101101)
print("query:",query)

#Queryで渡される値。Publisher側で指定している
binary_query = [int(i) for i in query]
print("binary_query:",binary_query)

com_key = binary_query*2
print("com_key:",com_key)

# spatial encode

#R
R_x, R_y = myfunc.input(com_key, R_array, bit_length)
print("R_x:",R_x)
print("R_y:",R_y)

#G
G_x, G_y = myfunc.input(com_key, G_array, bit_length)
print("G_x:",G_x)
print("G_y:",G_y)

#B
B_x, B_y = myfunc.input(com_key, B_array, bit_length)
print("B_x:",B_x)
print("B_y:",B_y)

# spatial encode
R = myfunc.spatial_encode(R_x, R_y, bit_length, r_intensity, LED_array_length)
G = myfunc.spatial_encode(G_x, G_y, bit_length, g_intensity, LED_array_length)
B = myfunc.spatial_encode(B_x, B_y, bit_length, b_intensity, LED_array_length)

image_array = myfunc.set_array(R, G, B , LED_array_length)
print(image_array)

time.sleep(5)
sense.clear()

#これを関数にする。入力X,Y,RGBで判定する