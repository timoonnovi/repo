import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setup(channel, GPIO.OUT)
chan_list = [21, 20, 16, 12, 7, 8, 25, 24]
#GPIO.setup(chan_list, GPIO.OUT)
#GPIO.output(channel, state)
#GPIO.cleanup()

#time.sleep()

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
    
a = int(input())
b = int(input())
lightNumber(a, b)
GPIO.cleanup()
