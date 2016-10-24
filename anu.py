#!/bin/python

"""
class dari awangga network util
"""
from scapy.all import ARP,Ether,sendp


class Anu(object):
	def sendArp(self,mac_rec,ip_rec,ip_target):	
		paket = Ether()/ARP(op="who-has",hwsrc=mac_rec,psrc=ip_rec,pdst=ip_target)
 		sendp(paket)
