#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID (Modified version from wascan)
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework

from re import search,I 

def sitelock(headers,content):
	detect = False
	detect |= search(r"SiteLock Incident ID",content) is not None
	if detect : 
		return "TrueShield Web Application Firewall (SiteLock)"
