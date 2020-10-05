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


argtab = (water1_temp_box.value,water2_temp_box.value,hv_battery_max_temp_box.value,hv_battery_avg_temp_box.value,esc_temp_box.value,motor_temp_box.value)

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

	test_num = number(180-10,68,72,win)
	test_num2 = number(257-10,68,72,win)
	flag = True

	mode_components[1].append(water1_temp_box)
	#loop
	global argtab
	x = threading.Thread(target=read_can, args=(argtab,),daemon=True)
	x.start()
	while(True):
		try:
			start_frame_time = time.time()

			#unwrap can table
			water1_temp_box.value,water2_temp_box.value,hv_battery_max_temp_box.value,hv_battery_avg_temp_box.value,esc_temp_box.value,motor_temp_box.value = argtab
			#click = win.checkMouse()
			#if click is not None:
			#mode = (mode + 1) % 2
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
			
			#testing values
			frame_counter+=1
			#water1_temp_box.value = frame_counter
			#revs.revs_value = (frame_counter*2500)%10000
			#revs.update_revs()
			if frame_counter%20==1:
				flag = not flag
				if not flag:
					test_num.display_number(2)
					test_num2.display_number(1)
				else:
					test_num.display_number(3)
					test_num2.display_number(7)
			#update all texts 
			for i in mode_components[current_mode]:
				if getattr(i,"update_filler",None):
					i.update_filler(1000-frame_counter)
					i.value_text.setText(str(round(i.value/i.top_value*100,2)))
				i.color_picker()
				if getattr(i,"check_warn",None):
					i.check_warn()
					i.value_text.setText(str(i.value))
			#end_frame_time = time.time()
			#frame_time = (end_frame_time-start_frame_time)
			#if frame_time > max_frame_time:
			#	print("OVERLOAD DETECTED! FRAMERATE IS TOO BIG!")
			#sleep(max_frame_time-frame_time if max_frame_time-frame_time > 0 else 1e-8)
			input()
		except GraphicsError as error:
			raise
			exit(0)

if __name__=="__main__":	
	main_loop(win)
