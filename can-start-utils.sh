#!/bin/sh
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 up
python3 ./dummy-can.py
