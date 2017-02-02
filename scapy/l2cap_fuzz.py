#!/usr/bin/env python2


from scapy.all import*
from scapy.layers import bluetooth
import bluetooth
import socket

print("Finding bluetooth devices....")
dev =  bluetooth.discover_devices() #This is to discover BLE devices
print("Scanning for devices")
print(dev[:])
print("Select device you want to test")
target = raw_input(">>>")


test1 = fuzz(L2CAP_CmdHdr())
test2 = fuzz(L2CAP_ConfReq())
test3 = fuzz(L2CAP_ConnReq())
test4 = fuzz(L2CAP_DisconnReq())
test5 = fuzz(L2CAP_Hdr())


print
print ("Bluetooth Fuzzer v1.2")
print
print (" 1 = L2CAP_CmdHdr")
print (" 2 = L2CAP_ConfReq")
print (" 3 = L2CAP_ConnReq")
print (" 4 = L2CAP_DisconnReq")
print (" 5 = L2CAP_Hdr")
print (" q = quit")
print
print (" Select a test")
print
select = raw_input(">")


if select == "1":
  while True:
    print(test1)
    srbt1(target, test1)
   
if select == "2":
  while True:
    print(test2)
    srbt1(target, test2)

if select == "3":
  while True:
    print(test3)
    srbt1(target, test3)

if select == "4":
  while True:
    print(test4)
    srbt1(target, test4)

if select == "5":
  while True:
    print(test5)
    srbt1(target, test5)
if select == "q":
	exit()
