""" 
sending and recieving response
"""
import scapy.all as sc

def scan(ip):
    
    arp_request= sc.ARP(pdst=ip)
    
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arp_request_broadcast = broadcast/arp_request
    
    #to send the packet we need to have the command
    
    sc.srp(arp_request_broadcast) #custom ether part
    
    #one of the output have answered packet and other will be having non answered
    
    #so we have to make two variables in order to record the output
    
    answered,unanswered = sc.srp(arp_request_broadcast,timeout=1)# when we mention the timeout that means that if it did not get reply it will exit the process
    #here we didnt mentioned the location of the packet but when we have mentioned the ether part we already made it aware to go to the every MAC adress 
    print(answered.summary())
    
    
    
scan("192.168.213.1/24")