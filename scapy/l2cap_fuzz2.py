#!/usr/bin/env python2


from scapy.all import*
from scapy.layers import bluetooth
import bluetooth
import socket

dev =  bluetooth.discover_devices() #This is to discover BLE devices
print("Scanning for devices")
print(dev[:])
print("Select device you want to test")
target = raw_input(">>>")
name = bluetooth.lookup_name(target)
print(name)
services = bluetooth.find_service(address=target)
print(services)
#sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#sock.connect((target, 4))
#sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)
#sock.connect((target,4))
while True:
	a = fuzz(L2CAP_ConnReq())
	srbt(target, a)


