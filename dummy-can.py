from can import *

bus = interface.Bus(bustype="socketcan", channel="vcan0")

while True:
    try:
        msg = bus.recv()
        print(type(msg.data.hex(' ',2)))
    except CanError:
        raise
        exit(0)