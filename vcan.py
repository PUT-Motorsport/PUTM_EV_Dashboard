from boxes import *
import can
import time
#from #dump import #dump
#from ptread import *
#from #dump import *


bustype = 'socketcan'
channel = 'vcan0'
bus = can.interface.Bus(channel=channel, bustype=bustype)
#constants:
speed_factor = 11/53
can_frame_hz = 20

draw_text = False

def read_can():
    with open("./error.log","a") as file:
        print("<+> TIMESTAMP: ",str(time.asctime()),file=file)
    while(True):
        try:
            message = bus.recv()
            alert_carrier = None
            hex_str = message.data.hex()
            if message.arbitration_id == 0x00d:
                water1_temp_box.value = int(hex_str[0]+hex_str[1],16)
                water2_temp_box.value = int(hex_str[2]+hex_str[3],16)
                #dump.water1_temp = int(hex_str[0:2],16)
                #dump.water2_temp = int(hex_str[2:4],16)
                #dump.back_state = int(hex_str[4:6],16)
            elif message.arbitration_id == 0x00c:
                hv_battery_max_temp_box.value = int(hex_str[14]+hex_str[15],16)
                hv_battery_avg_temp_box.value = int(hex_str[12]+hex_str[13],16)
                hv_battery_box.value = int(hex_str[10:12]+hex_str[8:10],16)
                #speedo.value = int(((int(hex_str[0:4],16)*speed_factor*3.141592*0.52)/60)*3.6)
                #print(speedo.value)
                alert_test = int(hex_str[6:8],16)
                if alert_test != 0:
                    alert.alert_carrier = "HV ERROR\n"+"0x"+hex_str[6:8].upper()
                    alert.alert_hv = True
                    with open("./error.log","a") as file:
                        print(str(time.asctime())+"    "+alert.alert_carrier+"\ncan frame:\n"+str(message.arbitration_id)+": "+hex_str,file=file)
                hv_battery_rms_box.value = int(hex_str[0:4],16)*int(hex_str[4:7],16)/1000
                #dump.hv_voltage = int(hex_str[0:3],16)
                #dump.hv_current = int(hex_str[3:6],16)
                #dump.hv_state = int(hex_str[6:8],16)
                #dump.hv_charge = int(hex_str[8:12],16)
                #dump.hv_temp_avg = int(hex_str[12:14],16)
                #dump.hv_temp_max = int(hex_str[14:16],16)
            elif message.arbitration_id == 0x00e:
                speedo.value = int(((int(hex_str[2:4]+hex_str[0:2],16)*speed_factor*3.141592*0.52)/60)*3.6)
                esc_temp_box.value = int(hex_str[14]+hex_str[15],16)
                motor_temp_box.value = int(hex_str[12]+hex_str[13],16)
                #dump.motor_rpm = int(hex_str[0:4],16)
                #dump.rms_current = int(hex_str[4:8],16)
                #dump.status = int(hex_str[8:12],16)
                #dump.motor_temp = int(hex_str[12:14],16)
                #dump.inverter_temp = int(hex_str[14:16],16)
            elif message.arbitration_id == 0x007:
                alert.alert_carrier = "INV. ERROR\n"+"0x"+hex_str.upper()
                alert.alert_hv = True
                with open("./error.log","a") as file:
                    print(str(time.asctime())+"    "+alert.alert_carrier+"\ncan frame:\n"+str(message.arbitration_id)+": "+hex_str,file=file)
            elif message.arbitration_id == 0x00b:
                lv_voltage = int(hex_str[0:2],16)/10
                lv_battery_box.secret_value = round(((lv_voltage-14)/2.8)*100,1)
                #print(lv_battery_box.secret_value)
                lv_battery_box.value = lv_voltage
                #print(lv_voltage,lv_battery_box.value)
                lv_battery_temp_box.value = int(hex_str[6:8],16)
                alert_test = int(hex_str[2:4],16)
                if alert_test != 0:
                    alert.alert_carrier = "LV ERROR "+"0x"+hex_str[2:4].upper()
                    with open("./error.log","a") as file:
                        print(str(time.asctime())+"    "+alert.alert_carrier+"\ncan frame:\n"+str(message.arbitration_id)+": "+hex_str,file=file)
                #dump.lv_voltage = int(hex_str[0:2],16)
                #dump.lv_state = int(hex_str[2:4],16)
                #dump.lv_temp_avg = int(hex_str[4:6],16)
                #dump.lv_temp_high = int(hex_str[6:8],16)
                #dump.lv_voltage_low = int(hex_str[8:10],16)
                #dump.lv_voltage_high = int(hex_str[10:12],16)
            elif message.arbitration_id == 0x00a:
                pass
                #water1_temp_box.value = int(hex_str[0:2],16)
                #dump.apps = int(hex_str[0:2],16)
            elif message.arbitration_id == 0x05a:
                pass
                #dump.steering_angle = int(hex_str[0:2],16)
                #dump.right_damper_front = int(hex_str[2:4],16)
                #dump.left_damper_front = int(hex_str[4:6],16)
                #dump.brake_pressure_front = int(hex_str[6:12],16)
                #dump.brake_pressure_back = int(hex_str[12:16],16)
            elif message.arbitration_id == 0x05c:
                pass
                #dump.wheel_speed_left = int(hex_str[0:4],16)
                #dump.wheel_speed_right = int(hex_str[4:8],16)
                #dump.right_damper_back = int(hex_str[8:10],16)
                #dump.left_damper_back = int(hex_str[10:12],16)
        except can.CanError as error:
            alert.alert_carrier = "CAN BUS ERROR"
def write_can():
    while(True):
        start = time.time()
        try:
            message = can.Message(data=[])
        except can.CanError as error:
            alert.alert_carrier = "CAN BUS ERROR"
        end = time.time()
        time.sleep(1/can_frame_hz-(end-start))
