# ARP_Poisoning_In_Python

**Demo Video**

[ARP cache poisoning attack](https://youtu.be/rRupkvxjj8I)

**Overview**

This program carries out ARP cache poisoning attack, also allowing a host to be the man-in-the-middle and intercept ongoing communication between two other hosts on the same local network.

**Environment Setup**

The environment was simulated by creating 3 virtual machines using [VirtualBox](https://www.virtualbox.org/wiki/VirtualBox). The virtual machines use Ubuntu 16.04 operating systems.
The virtual machine which is chosen to be the "man-in-the-middle" needs to have the following Python 2.7 package:

* [Scapy (2.2.0)](http://www.secdev.org/projects/scapy/doc/installation.html)

*Points to remember:*

* The 3 virtual machines need to be on the same local network. To ensure this, configure the network adapter to be "Bridged Adapter" for all 3 virtual machines.
* Command used to check local ARP cache table on each virtual machine: *arp -a*
* The program *arper.py* needs to be run on the "man-in-the-middle" machine with the format: 

  ```bash
  python arper.py <IPv4 address of victim1> <IPv4 address of victim2>
  ```
  **Example**
  ```bash
  python arper.py 192.168.0.1 192.168.0.2
  ```
