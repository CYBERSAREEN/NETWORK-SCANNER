""" 
NETWORK SCANNER

we need to write the command 
#>>>netdiscover -r <range of ip address> for example
"""
#>>>netdiscover -r 10.0.2.1/24(press q to quit)
""" 
ARP request  is basically a request made by the router to the system and system back to the router to establish a conection between two when there are many devices connected to it 
so if we go to the kali linux /windows and  type the command
arp -a
we can see the routers ip connecting to its mac address  
we will use scapy
"""
import scapy.all as sc

def scan(ip):
   
    sc.arping(ip)

scan("192.168.32.1/24")#taking random ip, /24 means scan all

#rout -n will tell the ip address

#create arp request directed to MAC address asking 

# for ip (we hve to make a packet)

# end the packet and wait for response

#analyse the response

#print result