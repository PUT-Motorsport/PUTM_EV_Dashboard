import can

def read_can(vars):
    bustype = 'socketcan'
    channel = 'can0'

    bus = can.interface.Bus(channel=channel, bustype=bustype)
    while(True):
        message = bus.recv()
        if message.arbitration_id == 0x00d:
            hex_str = message.data.hex()
            vars[0] = int(hex_str[0]+hex_str[1],16)
            vars[1] = int(hex_str[2]+hex_str[3],16)