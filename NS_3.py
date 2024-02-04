""" 
changing packet to broadcast form
"""
import scapy.all as sc

def scan(ip):
    
    arp_request= sc.ARP(pdst=ip)
    
    #(1) this will create a an ethernet object When performing an ARP scan, it is common to use a broadcast Ethernet frame because ARP requests are typically sent as broadcast messages. When a device wants to discover the MAC address associated with a specific IP address, it sends an ARP request to the entire local network by using a broadcast frame. 
    
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")#(2)and we have to set the destination 
    
    arp_request_broadcast = broadcast/arp_request #(3) The line packet = broadcast/arp_request combines the broadcast Ethernet frame (broadcast) with the ARP request packet (arp_request) to create a single packet that contains both the Ethernet frame and the ARP request. This combined packet is then sent over the network. 
    #(4) variablename.show() will show the detailed breakdown of each packet
    arp_request_broadcast.show()
    
    
    
scan("192.168.32.1/24")