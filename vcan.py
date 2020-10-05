import can

def read_can(vars):
    bustype = 'socketcan'
    channel = 'vcan0'

    bus = can.interface.Bus(channel=channel, bustype=bustype)
    while(True):
        message = bus.recv()
        hex_str = message.data.hex()
        if message.arbitration_id == 0x00d:
            vars[0] = int(hex_str[0]+hex_str[1],16)
            vars[1] = int(hex_str[2]+hex_str[3],16)
        elif message.arbitration_id == 0x00c:
            vars[2] = int(hex_str[14]+hex_str[15],16)
            vars[3] = int(hex_str[12]+hex_str[13],16)
        elif message.arbitration_id == 0x0e:
            vars[4] = int(hex_str[14]+hex_str[15],16)
            vars[5] = int(hex_str[12]+hex_str[13],16)