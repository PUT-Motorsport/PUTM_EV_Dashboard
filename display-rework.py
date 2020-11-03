#!/usr/bin/python3
#from math import *
#from random import randint
#from time import sleep as sleep
#from time import time as time

from graphics import *
from layout_rework import *
#from boxes import *
#from seven import *
from vcan import*

#import RPi.GPIO as GPIO

#import os
#import errno
import threading
#from copy import copy

mode_components = []
for i in range(3):
	mode_components.append([])

def undraw_mode(mode_components):
	for i in mode_components:
		i.undraw_components()
def draw_mode(mode_components):
	for i in mode_components:
		i.draw_components()


def main_loop(win):
	#setup
	frame_counter = 0
	mode = 0
	current_mode = 0
	#backdrop.undraw()
	win.setBackground("black")
	#max_frame_time = (1/framerate)
	change_flag = True

	#GPIO.setmode(GPIO.BCM)
	#GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_UP)

	mode_components[current_mode].append(water1_temp_box)
	mode_components[current_mode].append(water2_temp_box)
	mode_components[current_mode].append(lv_battery_box)
	mode_components[current_mode].append(lv_battery_temp_box)
	mode_components[current_mode].append(hv_battery_box)
	mode_components[current_mode].append(hv_battery_avg_temp_box)
	mode_components[current_mode].append(hv_battery_max_temp_box)
	mode_components[current_mode].append(esc_temp_box)
	mode_components[current_mode].append(hv_battery_rms_box)
	mode_components[current_mode].append(motor_temp_box)
	mode_components[current_mode].append(speedo)
	#test_num = number(180-10,68,72,win)
	#test_num2 = number(257-10,68,72,win)
	flag = True
	
	mode_components[1].append(water1_temp_box)
	#loop
	x = threading.Thread(target=read_can, args=(),daemon=True)
	x.start()
	while(True):
		try:
			#read = GPIO.input(26)
			#if  read == 0 and change_flag:
			#	mode = (mode + 1) % 2
			#	change_flag = False
			#elif read == 1:
			#	change_flag = True
			if mode == 0 and current_mode != 0:
				undraw_mode(mode_components[current_mode])
				current_mode = 0
				draw_mode(mode_components[current_mode])
				dump.text.undraw()
				bbb.undraw()
			#elif mode == 1 and current_mode != 1:
			#	undraw_mode(mode_components[current_mode])
			#	current_mode = 1
			#	bbb = Rectangle(Point(0,0),Point(480,320))
			#	bbb.setFill("black")
			#	bbb.draw(win)
			#	dump.text.draw(win)
			if alert.alert_carrier is not None and alert.alert_hv==False:
				if alert.alert_present==False:
					alert.alert_text.setText(alert.alert_carrier)
					alert.alert_present = True
					alert.current_alerts.append(alert.alert_carrier)
				elif alert.alert_carrier not in alert.current_alerts:
					alert.alert_text.setText(alert.alert_text.getText()+";"+alert.alert_carrier)
					alert.current_alerts.append(alert.alert_carrier)
			elif alert.alert_carrier is not None and alert.alert_hv==True:
				if alert.alert_carrier not in alert.current_alerts:
					alert.speedo.box = Rectangle(Point(alert.speedo.x,alert.speedo.y),Point(alert.speedo.x+alert.speedo.w,alert.speedo.y+alert.speedo.h))
					alert.speedo.box.setFill("red")
					alert.speedo.box.draw(win)
					text_alert = Text(Point(alert.speedo.x+alert.speedo.w/2,alert.speedo.y+alert.speedo.h/2),alert.alert_carrier)
					text_alert.setFill("white")
					text_alert.setSize(34)
					text_alert.draw(win)
					alert.current_alerts.append(alert.alert_carrier)
					alert.alert_hv=False

			#testing values
			frame_counter+=1
			for i in mode_components[current_mode]:
				if getattr(i,"update_filler",None):
					#i.update_filler(1000-frame_counter)
					if i.value is not None: i.update_filler()
					#i.value_text.setText(str(round(i.value/i.top_value*100,2)))
				#i.color_picker()
				if getattr(i,"check_warn",None):
					#if i==lv_battery_box:
				#		i.value_text.setText(i.secret_value)
				#	else:
					i.check_warn()
					i.value_text.setText(str(i.value))
				if getattr(i,"id_speed",None):
					if i.value == 666:
						speedo.value_text.setText("-")
					else:
						speedo.value_text.setText(str(speedo.value))
			#input()
			if mode == 1:
				dump.update()
		except GraphicsError as error:
			raise
			exit(0)

if __name__=="__main__":	
	main_loop(win)
