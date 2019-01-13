#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
import os, sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
volume=50
num=0
print('Progam start |OK|')
with open("stat.txt") as file:
    array = [row.strip() for row in file]
print('Stations list open |OK|')
os.popen('amixer  sset PCM  "'+str(volume)+'%"').read()
os.popen('killall -s 9 vlc').read()
os.popen('nvlc '+array[num]+' -d')
print('Starting nvls services |OK|')
while True:
	if GPIO.input(5):
		volume=volume
	else:
		volume=volume+5
		os.popen('amixer  sset PCM  "'+str(volume)+'%"').read()
		print('Volume set : '+str(volume))
	if GPIO.input(6):
		volume=volume
	else:
		volume=volume-5
		os.popen('amixer  sset PCM  "'+str(volume)+'%"').read()
		print('Volume set : '+str(volume))
	if GPIO.input(7):
		num=num
	else:
		if num<1:
			num=num
		else:
			num=num-1
			os.popen('killall -s 9 vlc').read()
			os.popen('nvlc '+array[num]+' -d')
			print('Station : '+str(num))
	if GPIO.input(8):
		num=num
	else:
		if num>=(len(array)-1):
			num=num
		else:
			num=num+1
			os.popen('killall -s 9 vlc').read()
			os.popen('nvlc '+array[num]+' -d')
			print('Station : '+str(num))
	sleep(0.1)