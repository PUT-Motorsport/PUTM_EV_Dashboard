import can

bustype = 'socketcan'
channel = 'vcan0'

bus = can.interface.Bus(channel=channel, bustype=bustype)
while(True):
    with open("./test_pipe","w") as f:
        message = bus.recv()
        if message.arbitration_id == 0x042:
            print("LVT",int(message.data.hex(),16),file=f)
            print("LVT",int(message.data.hex(),16))