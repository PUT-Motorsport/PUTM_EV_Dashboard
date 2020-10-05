import can

def read_can(vars):
    bustype = 'socketcan'
    channel = 'vcan0'

    bus = can.interface.Bus(channel=channel, bustype=bustype)
    while(True):
        message = bus.recv()
        if message.arbitration_id == 0x00d:
            hex_str = message.data.hex()
            vars[0] = int(hex_str[0]+hex_str[1],16)
            vars[1] = int(hex_str[2]+hex_str[3],16)
        elif message.arbitration_id == 0x00c:
            vars[2] = int(hex_str[14]+hex_str[15],16)
            vars[3] = int(hex_str[12]+hex_str[13],16)
            vars[6] = float(hex_str[0]+hex_str[1]+hex_str[2]+hex_str[3]+hex_str[4]+hex_str[5],16) \
            *float(hex_str[6]+hex_str[7]+hex_str[8]+hex_str[9]+hex_str[10]+hex_str[11],16)
        elif message.arbitration_id == 0x00e:
            vars[4] = int(hex_str[14]+hex_str[15],16)
            vars[5] = int(hex_str[12]+hex_str[13],16)