""" 
sending and recieving response
"""
import scapy.all as sc

def scan(ip):
    
    arp_request= sc.ARP(pdst=ip)
    
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arp_request_broadcast = broadcast/arp_request
    
    answered_list = sc.srp(arp_request_broadcast,timeout=1,verbose=False)[0]#verbose = false means that i dont want to see the aditional information
    print("IP\t\t\tMAC ADDRESS\n-----------------------------------")
    for element in answered_list:
        print(element[1].psrc,end="\t\t\t")#to print the ip address
        print(element[1].hwsrc)#to print the mac address of  the client
        
        print("----------------------------------- ")
    
    
scan("192.168.213.1/24")