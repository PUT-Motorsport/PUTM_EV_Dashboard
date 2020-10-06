#!/usr/bin/python3
from math import *
from random import randint
from time import sleep as sleep
from time import time as time

from graphics import *
from layout_rework import *
from boxes import *
from seven import *
from vcan import*

import os
import errno
import threading
from copy import copy

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
	win.setBackground("black")
	#max_frame_time = (1/framerate)

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

	#test_num = number(180-10,68,72,win)
	#test_num2 = number(257-10,68,72,win)
	flag = True

	mode_components[1].append(water1_temp_box)
	#loop
	x = threading.Thread(target=read_can, args=(),daemon=True)
	x.start()
	while(True):
		try:
			if mode == 0 and current_mode != 0:
				undraw_mode(mode_components[current_mode])
				water1_temp_box.move_components(-100,-100)
				current_mode = 0
				draw_mode(mode_components[current_mode])
			elif mode == 1 and current_mode != 1:
				undraw_mode(mode_components[current_mode])
				water1_temp_box.move_components(100,100)
				current_mode = 1
				draw_mode(mode_components[current_mode])
			
			if alert.alert_carrier is not None:
				if alert.alert_present==False:
					alert.alert_text.setText(alert.alert_carrier)
					alert.alert_present = True
					alert.current_alerts.append(alert.alert_carrier)
				elif alert.alert_carrier not in alert.current_alerts:
					alert.alert_text.setText(alert.alert_text.getText()+";"+alert.alert_carrier)
					alert.current_alerts.append(alert.alert_carrier)
			#testing values
			frame_counter+=1
			for i in mode_components[current_mode]:
				if getattr(i,"update_filler",None):
					#i.update_filler(1000-frame_counter)
					if i.value is not None: i.update_filler()
					#i.value_text.setText(str(round(i.value/i.top_value*100,2)))
				i.color_picker()
				if getattr(i,"check_warn",None):
					i.check_warn()
					i.value_text.setText(str(i.value))
			#input()
		except GraphicsError as error:
			raise
			exit(0)

if __name__=="__main__":	
	main_loop(win)
