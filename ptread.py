import smbus
import time

def read_pt1():
    address = 0x48
    A0 = 0x40
    A1 = 0x41
    A2 = 0x42
    A3 = 0x43
    bus = smbus.SMBus(1)
    bus.write_byte(address,A3)        
    value = bus.read_byte(address)
    voltage_diffs = []
    print(3.3-value)
    value = %(value*3.3/255)
    for i in range(12):
        voltage_diffs.append((abs(value-((3.3/12)*(i+1))),i))
        #voltage_diffs[i][0]
    voltage_diffs.sort(key=lambda x: x[0])
    return voltage_diffs[0][1]
if __name__=="__main__":
    print(read_pt1())
