from boxes import *
import can



def read_can():
    bustype = 'socketcan'
    channel = 'can0'

    #constants:
    speed_factor = 11/53
    
    bus = can.interface.Bus(channel=channel, bustype=bustype)
    while(True):
        try:
            message = bus.recv()
            alert_carrier = None
            hex_str = message.data.hex()
            print("success")
            if message.arbitration_id == 0x00d:
                water1_temp_box.value = int(hex_str[0]+hex_str[1],16)
                water2_temp_box.value = int(hex_str[2]+hex_str[3],16)
            elif message.arbitration_id == 0x00c:
                hv_battery_max_temp_box.value = int(hex_str[14]+hex_str[15],16)
                hv_battery_avg_temp_box.value = int(hex_str[12]+hex_str[13],16)
                hv_battery_box.value = int(hex_str[8:12],16)
                speedo.value = int(int(hex_str[0:5],16)*speed_factor)
            elif message.arbitration_id == 0x0e:
                esc_temp_box.value = int(hex_str[14]+hex_str[15],16)
                motor_temp_box.value = int(hex_str[12]+hex_str[13],16)
        except can.CanError as error:
            alert.alert_carrier = "CAN BUS ERROR"
