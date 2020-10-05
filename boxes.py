from graphics import *
from layout_rework import *
from math import floor

class temp_box:
	def __init__(self,x,y,w,h,font_size,text_str,win):
		self.left_point = Point(x,y)
		self.right_point = Point(x+w,y+h)
		self.warn = False
		self.tick = False
		self.text = Text(Point(x+w/2,y+15),text_str)
		self.text.setTextColor("white")
		self.text.setFace("helvetica")
		self.text.setSize(font_size)
		self.text.setStyle("bold")
		self.box = Rectangle(self.left_point,self.right_point)
		self.box.setOutline("white")
		self.box.setWidth(1)
		self.win = win
		self.value = None
		self.max_safe_value = None
		self.value_text = Text(Point(x+w/2,y+h-15),self.value)
		self.value_text.setTextColor("white")
		self.value_text.setFace("helvetica")
		self.value_text.setSize(font_size+8)
		self.value_text.setStyle("bold")
	def draw_components(self):
		self.box.draw(self.win)
		self.text.draw(self.win)
		self.value_text.draw(self.win)
	def undraw_components(self):
		self.box.undraw()
		self.text.undraw()
		self.value_text.undraw()
	def move_components(self,x,y):
		self.box.move(x,y)
		self.text.move(x,y)
		self.value_text.move(x,y)
	def color_picker(self):	
		pass
		#if self.value is not None and self.max_safe_value is not None:
		#	if self.value < 0.5*self.max_safe_value:
		#		self.text.setTextColor(color_rgb(100,255,100))
		#		self.warn = False
		#	elif self.value >= 0.5*self.max_safe_value and self.value < 0.8*self.max_safe_value:
		#		self.text.setTextColor("orange")
		#		self.warn = False
		#	elif self.value >= self.max_safe_value:
		#		self.warn = True
		#	else:
		#		self.text.setTextColor("red")
		#		self.warn = False
	def check_warn(self):
		if self.warn:
			if self.tick:
				self.text.setTextColor("black")
			else:
				self.text.setTextColor("red")
			self.tick = not self.tick
class fill_box:
	def __init__(self,x,y,w,h,font_size,text_str,win):
		self.h = h
		self.y=y
		self.w=w
		self.left_point = Point(x,y)
		self.right_point = Point(x+w,y+h)
		self.fill_left_point = Point(x+1,y+1)
		self.fill_right_point = Point(x+w-1,y+h-1)
		self.text = Text(Point(x+w/2,y+15),text_str)
		self.text.setTextColor("white")
		self.text.setFace("helvetica")
		self.text.setSize(font_size)
		self.text.setStyle("bold")
		self.box = Rectangle(self.left_point,self.right_point)
		self.box.setOutline("white")
		self.box.setWidth(1)
		self.win = win
		self.top_value = None
		self.value = None
		#self.filler = Rectangle(self.fill_left_point,self.fill_right_point)
		self.fillers = []
		for i in range(50):
			self.fillers.append(Rectangle(Point(self.left_point.getX(),self.y+(self.h/50)*i),Point(self.left_point.getX()+self.w,self.y+(self.h/50)*(i+1))))
			self.fillers[i].setFill("green")
			self.fillers[i].setOutline("green")
			self.fillers[i].draw(win)
		self.value_text = Text(Point(x+w/2,y+h-15),self.value)
		self.value_text.setTextColor("white")
		self.value_text.setFace("helvetica")
		self.value_text.setSize(font_size+2)
		self.value_text.setStyle("bold")
		self.last_undrawn = None
	def draw_components(self):
		#self.filler.draw(self.win)
		self.box.draw(self.win)
		self.text.draw(self.win)
		self.value_text.draw(self.win)
	def undraw_components(self):
		self.box.undraw()
		#self.filler.undraw()
		self.text.undraw()
		self.value_text.undraw()
	def move_components(self,x,y):
		self.box.move(x,y)
		self.filler.move(x,y)
		self.text.move(x,y)
		self.value_text.move(x,y)
	def redraw_text(self):
		self.text.undraw()
		self.value_text.undraw()
		self.text.draw(self.win)
		self.value_text.draw(self.win)
	def update_filler(self,x):
		if self.value is None:
			self.value = x
		temp = (x/self.top_value)
		delta = temp-(self.value/self.top_value)
		#print(delta)
		if delta <= -0.02:
			#print("abs: ",floor(delta/(-0.02)))
			i=0
			if self.last_undrawn is not None:
				for i in range(floor(delta/(-0.02))):
					self.fillers[self.last_undrawn+i].undraw()
				self.last_undrawn += floor(delta/(-0.02))
			else:
				for i in range(floor(delta/(-0.02))):
					self.fillers[i].undraw()
				self.last_undrawn = floor(delta/(-0.02))
			#print("last: ", self.last_undrawn)
			self.value = x
		#px_delta = abs(self.filler.getP1().getY()-self.fill_left_point.getY() - (self.h*(1-self.value)))
		#if px_delta >= 1:
		#	self.filler.undraw()
		#	self.filler = Rectangle(Point(self.fill_left_point.getX(),
		#		self.fill_left_point.getY()+(self.h*(1-self.value))),
		#			self.fill_right_point)
		#	self.filler.draw(self.win)
		#	self.redraw_text()
	def color_picker(self):
		pass
		#if self.value is not None:
		#	if self.value > 0.5:
		#		self.filler.setFill(color_rgb(0,100,0))
		#	elif self.value <= 0.5 and self.value > 0.2:
		#		self.filler.setFill("orange")
		#	else:
		#		self.filler.setFill("red")
class fill_box_h:
	def __init__(self,x,y,w,h,font_size,text_str,win):
		self.h = h
		self.y=y
		self.w=w
		self.h=h
		self.x=x
		self.text_str = text_str
		self.left_point = Point(x,y)
		self.right_point = Point(x+w,y+h)
		self.fill_left_point = Point(x+1,y+1)
		self.fill_right_point = Point(x+w-1,y+h-1)
		self.text = Text(Point(x+w/2,y+15),text_str)
		self.text.setTextColor("white")
		self.text.setFace("helvetica")
		self.text.setSize(font_size)
		self.text.setStyle("bold")
		self.box = Rectangle(self.left_point,self.right_point)
		self.box.setOutline("white")
		self.box.setWidth(1)
		self.win = win
		self.top_value = None
		self.value = None
		#self.filler = Rectangle(self.fill_left_point,self.fill_right_point)
		self.fillers = []
		for i in range(50):
			#self.fillers.append(Rectangle(Point(self.left_point.getX(),self.y+(self.h/50)*i),Point(self.left_point.getX()+self.w,self.y+(self.h/50)*(i+1))))
			self.fillers.append(Rectangle(Point(self.x+(self.w/50)*i,self.left_point.getY()),Point(self.x+(self.h/50)*(i+1),self.left_point.getY()+self.h)))
			self.fillers[i].setFill("green")
			self.fillers[i].setOutline("green")
			self.fillers[i].draw(win)
		self.fillers.reverse()
		self.value_text = Text(Point(x+w/2,y+h-15),self.value)
		self.value_text.setTextColor("white")
		self.value_text.setFace("helvetica")
		self.value_text.setSize(font_size+2)
		self.value_text.setStyle("bold")
		self.last_undrawn = None
	def draw_components(self):
		#self.filler.draw(self.win)
		self.box.draw(self.win)
		self.text.draw(self.win)
		self.value_text.draw(self.win)
	def undraw_components(self):
		self.box.undraw()
		#self.filler.undraw()
		self.text.undraw()
		self.value_text.undraw()
	def move_components(self,x,y):
		self.box.move(x,y)
		self.filler.move(x,y)
		self.text.move(x,y)
		self.value_text.move(x,y)
	def redraw_text(self):
		self.text.undraw()
		self.value_text.undraw()
		self.text.draw(self.win)
		self.value_text.draw(self.win)
	def update_filler(self,x):
		if self.value is None:
			self.value = x
		temp = (x/self.top_value)
		delta = temp-(self.value/self.top_value)
		#print(delta)
		if delta <= -0.02:
			#print("abs: ",floor(delta/(-0.02)))
			i=0
			if self.last_undrawn is not None:
				for i in range(floor(delta/(-0.02))):
					self.fillers[self.last_undrawn+i].undraw()
				self.last_undrawn += floor(delta/(-0.02))
			else:
				for i in range(floor(delta/(-0.02))):
					self.fillers[i].undraw()
				self.last_undrawn = floor(delta/(-0.02))
			#print("last: ", self.last_undrawn)
			self.value = x
		#px_delta = abs(self.filler.getP1().getY()-self.fill_left_point.getY() - (self.h*(1-self.value)))
		#if px_delta >= 1:
		#	self.filler.undraw()
		#	self.filler = Rectangle(Point(self.fill_left_point.getX(),
		#		self.fill_left_point.getY()+(self.h*(1-self.value))),
		#			self.fill_right_point)
		#	self.filler.draw(self.win)
		#	self.redraw_text()
	def color_picker(self):
		pass
		#if self.value is not None:
		#	if self.value > 0.5:
		#		self.filler.setFill(color_rgb(0,100,0))
		#	elif self.value <= 0.5 and self.value > 0.2:
		#		self.filler.setFill("orange")
		#	else:
		#		self.filler.setFill("red")

class rev:
	def __init__(self):
		self.rev_origin_point = Point(10,30)
		self.revs_value = 10000
		self.max_revs = 6000 #for now
		self.drawn_labels = 99
		self.rev_label_num = 6
		self.rev_labels = [Text(Point(10+(i*460/self.rev_label_num),10),str(int(i*self.max_revs/self.rev_label_num/1000))) for i in range(self.rev_label_num+1)]
		self.rev_lines = [Line(Point(10+(i*460/self.rev_label_num),18),Point(10+(i*460/self.rev_label_num),30)) for i in range(self.rev_label_num+1)]
		for i in self.rev_labels:
			i.setFill("white")
			i.draw(win)
		for i in self.rev_lines:
			i.setFill("white")
			i.draw(win)
		#self.rev_box = Rectangle(self.rev_origin_point,Point(10+460*self.revs_value/self.max_revs,50))
		#self.rev_box.setFill("white")
		#self.rev_box.setOutline("white")
		#self.rev_box.draw(win)
		self.rev_boxes = []
		for i in range(99):
			self.rev_boxes.append(Rectangle(Point(self.rev_origin_point.getX()+10+4.6*i,self.rev_origin_point.getY()),Point(10+4.6*i,self.rev_origin_point.getY()+30)))
			self.rev_boxes[i].setFill("white")
			self.rev_boxes[i].setOutline("white")
			self.rev_boxes[i].draw(win)
	def update_revs(self):
		max_i = int((self.revs_value/self.max_revs) * 99)
		if max_i > self.drawn_labels:
			for i in range(self.drawn_labels,max_i):
				self.rev_boxes[i].draw(win)
				#print(i,max_i)
		else:
			#for i in range(max_i,self.drawn_labels):
			#	self.rev_boxes[i].undraw()
			for i in range(max_i,self.drawn_labels):
				self.rev_boxes[(self.drawn_labels-1)-i+max_i].undraw()
				#print(i,max_i)
		self.drawn_labels = max_i
		#self.rev_box.undraw()
		#self.rev_box = Rectangle(self.rev_origin_point,Point(10+460*self.revs_value/self.max_revs,50))
		#self.rev_box.setFill("white")
		#self.rev_box.setOutline("white")
		#self.rev_box.draw(win)

class speed:
	def __init__(self,x,y,w,h,speed_value,win):
		self.box = Rectangle(Point(x,y),Point(x+w,y+h))
		self.box.setOutline("White")
		self.value = speed_value
		self.value_text = Text(Point(x+(w/2),y+(h/2+4)),str(self.value))
		self.win = win
	def draw_components(self):
		self.box.draw(self.win)
		self.value_text.draw(self.win)
	def undraw_components(self):
		self.box.undraw()
		self.value_text.undraw()
	def update_filler(self,x):
		self.value = x 
		self.value_text.setText(str(self.value))
#global window declaration - don't know what to do with it honestly
win = GraphWin("This is not a Raspberry, come on",screen_w,screen_h)

# all the boxes. ALL OF THEM FOR ALL MODES ARE DECLARED AND INITED HERE 
# (MOVE LIMITS TO limits.py for easy management by teammates)



#water1 temp box
water1_temp_box = temp_box(95,240,75,50,8,"WATER 1",win)
water1_temp_box.draw_components()
water1_temp_box.box.setOutline("white")
water1_temp_box.max_safe_value = 100

#water2 temp box
water2_temp_box = temp_box(310,240,75,50,8,"WATER 2",win)
water2_temp_box.draw_components()
water2_temp_box.box.setOutline("white")
water2_temp_box.max_safe_value = 100
water2_temp_box.value = 0

#LV Battery indicator box
lv_battery_box = fill_box_h(10,150-80,75,50,8,"LV BATT",win)
lv_battery_box.draw_components()
lv_battery_box.box.setOutline("white")
lv_battery_box.top_value = 1000

#LV Battery temp box
lv_battery_temp_box = temp_box(10,150-20,75,50,8,"LV TEMP",win)
lv_battery_temp_box.draw_components()
lv_battery_temp_box.box.setOutline("white")
lv_battery_temp_box.max_safe_value = 80
lv_battery_temp_box.value = 0

#HV battery indicator BIG BOX
hv_battery_box = fill_box_h(10,185,460,50,8,"HV BATT CHARGE",win)
hv_battery_box.draw_components()
#hv_battery_box.text = Text(Point(hv_battery_box.x+hv_battery_box.w/2-100,hv_battery_box.y+15),hv_battery_box.text_str)
hv_battery_box.box.setOutline("white")
hv_battery_box.top_value = 1000

#HV AVG temp box
hv_battery_avg_temp_box = temp_box(395,210-60-20,75,50,8,"HV TEMP",win)
hv_battery_avg_temp_box.draw_components()
hv_battery_avg_temp_box.box.setOutline("white")
hv_battery_avg_temp_box.max_safe_value = 80
hv_battery_avg_temp_box.value = 0

#HV MAX temp box
hv_battery_max_temp_box = temp_box(240-75/2,240,75,50,8,"HV MAX",win)
hv_battery_max_temp_box.draw_components()
hv_battery_max_temp_box.box.setOutline("white")
hv_battery_max_temp_box.max_safe_value = 80
hv_battery_max_temp_box.value = 0

#RMS kW
hv_battery_rms_box = temp_box(10,240,75,50,8,"HV kW",win)
hv_battery_rms_box.draw_components()
hv_battery_rms_box.box.setOutline("white")
hv_battery_rms_box.max_safe_value = 300
hv_battery_rms_box.value = 0

#ESC temp box
esc_temp_box = temp_box(395,240,75,50,8,"ESC TEMP",win)
esc_temp_box.draw_components()
esc_temp_box.box.setOutline("white")
esc_temp_box.max_safe_value = 80
esc_temp_box.value = 0

#MOTOR temp box
motor_temp_box = temp_box(395,90-20,75,50,8,"MTR TEMP",win)
motor_temp_box.draw_components()
motor_temp_box.box.setOutline("white")
motor_temp_box.max_safe_value = 80
motor_temp_box.value = 0

#Generic RED ALERT TEXT
alert_text = Text(Point(240,310),"RUDA ZJADŁA PODŁOGE")
alert_text.setTextColor(color_rgb(255,75,65))
alert_text.setFace("helvetica")
alert_text.setSize(16)
alert_text.draw(win)

#Revs
revs = rev()

#speed
speedo = speed(240-(300/2),65,300,135-20,300,win)
speedo.value_text.setFill("black")
speedo.value_text.setSize(35)
speedo.draw_components()