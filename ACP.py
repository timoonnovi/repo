import RPi.GPIO as GPIO
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

GPIO.setmode(GPIO.BCM)
#GPIO.setup(channel, GPIO.OUT)
#chan_list = [21, 20, 16, 12, 7, 8, 25, 24]
chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
#GPIO.setup(chan_list, GPIO.OUT)
#GPIO.output(channel, state)
#GPIO.cleanup()

#time.sleep()

#samplerate, data = wavfile.read('./output/audio.wav')

def lightUp(ledNumber, period):
    GPIO.setup(ledNumber, GPIO.OUT)
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)
def lightDown(ledNumber, period):
    GPIO.setup(ledNumber, GPIO.OUT)
    GPIO.output(ledNumber, 0)
    time.sleep(period)
    GPIO.output(ledNumber, 1)
def blink(ledNumber, blinkCount, lightPeriod, darkPeriod):
    for i in range(blinkCount):
        lightUp(ledNumber, lightPeriod)
        time.sleep(darkPeriod)
def runningLight(count, period):
    xyu = 0
    while xyu < count:
        lightUp(chan_list[xyu%len(chan_list)], period)
        xyu += 1
def runningDark(count, period):
    xyu = 0
    for led in chan_list:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, 1)
    while xyu < count:
        lightDown(chan_list[xyu%len(chan_list)], period)
        xyu += 1
def decToBinList(decNumber):
    xyu = bin(decNumber)
    st = xyu[2:]
    while len(st) < 8:
        st = str(0) + st
    return st
def lightNumber(number, period):
    xyu = decToBinList(number)
    for i in range(8):
        if str(xyu[i])==str(1):
            GPIO.setup(chan_list[i], GPIO.OUT)
            GPIO.output(chan_list[i], 1)
    
    time.sleep(period)
    for i in range(8):
        GPIO.setup(chan_list[i], GPIO.OUT)
        GPIO.output(chan_list[i], 0)
def runningPattern(pattern, direction):
    while True:
        lightNumber(pattern, 1)
        if direction > 0:
            tmp = pattern % 2
            pattern = pattern >> 1
            pattern += tmp*128
        else:
            tmp = pattern // 128
            pattern = pattern << 1
            pattern -= 256
            pattern += tmp
            
def repetitionsNumber(a, t=0):
    for i in range(a):
        for j in range(256):
            lightNumber(j, t)
        for j in range(256, -1, -1):
            lightNumber(j, t)
            
def nox():
    for i in chan_list:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, 0)

            
def sinout(fr=0, hr=0):
    a=[]
    ti=[]
    t_0=time.time()
    for i in range(hr):
        t=(time.time()-t_0)*(1/(fr*0.0001))
        time.sleep(0.0001)
        a.append(int((math.sin(t*3.1415)+1)*128))
        ti.append(t)
        
#    plt.plot(ti, a)
#    plt.show()
    return a

def sinCAP(a, b, fr):
    c=sinout(a, b)
    for i in range(b):
        lightNumber(c[i], 1/(fr*a))
    
def Volt(a):
    xyu = decToBinList(a)
    for i in range(8):
        if str(xyu[i]) == str(1):
            GPIO.setup(chan_list[i], GPIO.OUT)
            GPIO.output(chan_list[i], 1)
    
def VoltPodbor():
    GPIO.setup(4, GPIO.IN)
    c=GPIO.input(4)
    a = 0
    while a < 256:
        Napr(a)
        c = GPIO.input(4)
        if c == 1:
            a += 1
        else:
            break
    return a
    nox()
#lightNumber(b, a)
#repetitionsNumber(b, a)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)

while 1:
    print("Enter value (-1 to exit) > ", end = '')
    a = int(input())
    if a == -1:
        nox()
        exit()
    print(a, " = ", round(a*3.3/255, 2), "V", sep = '')
    nox()
    Volt(a)
    
GPIO.cleanup()
                                                                                                                                            