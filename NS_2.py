""" 
Designing an algorithm tp discover clients on the same Netework
"""
import scapy.all as sc

def scan(ip):
    
    arp_request= sc.ARP(pdst=ip) #(7) or we can type it as 
    
    #(5) one menthod is to set pdst which we have to alter is
    
    #(6) arp_request.pdst=ip
    
    #(1) if we have to get summary of any object we made out of scapy class we have to write the command print (nameof the variable.summary())
    
    print(arp_request.summary())#(2) ARP who has 0.0.0.0 says 10.0.2.8 is to be in the format that our ip address shall ask not the 0.0.0.0
    
    #(3) so we need to make the ip get the way to the command
    
    #(4) sc.ls(sc.name o the class())  will give the name of the field we can work on to 
    
scan("192.168.32.1/24")