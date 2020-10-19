from graphics import *
from varname import nameof

class Dump:
    def __init__(self):
        self.apps = None
        self.frame1_str = nameof(self.apps)+": "+str(self.apps)+"# "
        
        self.lv_voltage = None
        self.lv_state = None
        self.lv_temp_avg = None
        self.lv_temp_high = None
        self.lv_voltage_low = None
        self.lv_voltage_high = None
        self.frame2_str = nameof(self.lv_voltage)+": "+str(self.lv_voltage)+"# "+nameof(self.lv_state)+": "+str(self.lv_state)+"\n"+nameof(self.lv_temp_avg)+": "+str(self.lv_temp_avg)+"\n"+nameof(self.lv_temp_high)+": "+str(self.lv_temp_high)+"\n"+nameof(self.lv_voltage_low)+": "+str(self.lv_voltage_low)+"# "+nameof(self.lv_voltage_high)+": "+str(self.lv_voltage_high)+"\n"
        
        self.hv_voltage = None
        self.hv_current = None
        self.hv_state = None
        self.hv_charge = None
        self.hv_temp_avg = None
        self.hv_temp_max = None
        self.frame3_str = nameof(self.hv_voltage)+": "+str(self.hv_voltage)+"# "+nameof(self.hv_current)+": "+str(self.hv_current)+"# "+nameof(self.hv_state)+": "+str(self.hv_state)+"\n"+nameof(self.hv_charge)+": "+str(self.hv_charge)+"# "+nameof(self.hv_temp_avg)+": "+str(self.hv_temp_avg)+"# "+nameof(self.hv_temp_max)+": "+str(self.hv_temp_max)+"\n"

        self.water1_temp = None
        self.water2_temp = None
        self.back_state = None
        self.frame4_str = nameof(self.water1_temp)+": "+str(self.water1_temp)+"# "+nameof(self.water2_temp)+": "+str(self.water2_temp)+"# "+nameof(self.back_state)+": "+str(self.back_state)+"\n"

        self.motor_rpm = None
        self.rms_current = None
        self.status = None
        self.motor_temp = None
        self.inverter_temp = None
        self.frame5_str = nameof(self.motor_rpm)+": "+str(self.motor_rpm)+"# "+nameof(self.rms_current)+": "+str(self.rms_current)+"# "+nameof(self.status)+": "+str(self.status)+"\n"+nameof(self.motor_temp)+": "+str(self.motor_temp)+"# "+nameof(self.inverter_temp)+": "+str(self.inverter_temp)+"\n"

        self.steering_angle = None
        self.right_damper_front = None
        self.left_damper_front = None
        self.brake_pressure_front = None
        self.brake_pressure_back = None
        self.frame6_str = nameof(self.steering_angle)+": "+str(self.steering_angle)+"\n"+nameof(self.right_damper_front)+": "+str(self.right_damper_front)+"# "+nameof(self.left_damper_front)+": "+str(self.left_damper_front)+"\n"+nameof(self.brake_pressure_front)+": "+str(self.brake_pressure_front)+"# "+nameof(self.brake_pressure_back)+": "+str(self.brake_pressure_back)+"\n"

        self.wheel_speed_left = None
        self.wheel_speed_right = None
        self.right_damper_back = None
        self.left_damper_back = None
        self.frame7_str = nameof(self.wheel_speed_left)+": "+str(self.wheel_speed_left)+"# "+nameof(self.wheel_speed_right)+": "+str(self.wheel_speed_right)+"\n"+nameof(self.right_damper_back)+": "+str(self.right_damper_back)+"# "+nameof(self.left_damper_back)+": "+str(self.left_damper_back)+"\n"

        self.text = Text(Point(240,160),self.frame1_str+self.frame2_str+self.frame3_str+self.frame4_str+self.frame5_str+self.frame6_str+self.frame7_str)
        self.text.setFace("helvetica")
        self.text.setSize(12)
        self.text.setFill("white")
        self.text.setStyle("bold")
    def update(self):
        self.frame1_str = nameof(self.apps)+": "+str(self.apps)+"# "
        self.frame2_str = nameof(self.lv_voltage)+": "+str(self.lv_voltage)+"# "+nameof(self.lv_state)+": "+str(self.lv_state)+"\n"+nameof(self.lv_temp_avg)+": "+str(self.lv_temp_avg)+"\n"+nameof(self.lv_temp_high)+": "+str(self.lv_temp_high)+"\n"+nameof(self.lv_voltage_low)+": "+str(self.lv_voltage_low)+"# "+nameof(self.lv_voltage_high)+": "+str(self.lv_voltage_high)+"\n"
        self.frame3_str = nameof(self.hv_voltage)+": "+str(self.hv_voltage)+"# "+nameof(self.hv_current)+": "+str(self.hv_current)+"# "+nameof(self.hv_state)+": "+str(self.hv_state)+"\n"+nameof(self.hv_charge)+": "+str(self.hv_charge)+"# "+nameof(self.hv_temp_avg)+": "+str(self.hv_temp_avg)+"# "+nameof(self.hv_temp_max)+": "+str(self.hv_temp_max)+"\n"
        self.frame4_str = nameof(self.water1_temp)+": "+str(self.water1_temp)+"# "+nameof(self.water2_temp)+": "+str(self.water2_temp)+"# "+nameof(self.back_state)+": "+str(self.back_state)+"\n"
        self.frame5_str = nameof(self.motor_rpm)+": "+str(self.motor_rpm)+"# "+nameof(self.rms_current)+": "+str(self.rms_current)+"# "+nameof(self.status)+": "+str(self.status)+"\n"+nameof(self.motor_temp)+": "+str(self.motor_temp)+"# "+nameof(self.inverter_temp)+": "+str(self.inverter_temp)+"\n"
        self.frame6_str = nameof(self.steering_angle)+": "+str(self.steering_angle)+"\n"+nameof(self.right_damper_front)+": "+str(self.right_damper_front)+"# "+nameof(self.left_damper_front)+": "+str(self.left_damper_front)+"\n"+nameof(self.brake_pressure_front)+": "+str(self.brake_pressure_front)+"# "+nameof(self.brake_pressure_back)+": "+str(self.brake_pressure_back)+"\n"
        self.frame7_str = nameof(self.wheel_speed_left)+": "+str(self.wheel_speed_left)+"# "+nameof(self.wheel_speed_right)+": "+str(self.wheel_speed_right)+"\n"+nameof(self.right_damper_back)+": "+str(self.right_damper_back)+"# "+nameof(self.left_damper_back)+": "+str(self.left_damper_back)+"\n"
        self.text.setText(self.frame1_str+self.frame2_str+self.frame3_str+self.frame4_str+self.frame5_str+self.frame6_str+self.frame7_str)






dump = Dump()
