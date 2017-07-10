#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket
import time

def scan(ip,port):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket()
        s.connect((ip,port))
        return True
    except:
        return

def scanport():
    domain = raw_input("Please input your target:")
    ip = socket.gethostbyname(domain)
    print 'ip: %s' % ip
    portlist = [80,8080,9090,3306,3389]
    starttime = time.time()
    for port in portlist:
        res = scan(ip,port)
        if res:
            print 'this port:%s is on' % port
    endtime = time.time()
    print "This scan spent %s" %(endtime - starttime)

if __name__ == '__main__':
    scanport()


"""
Please input your target:192.168.86.194
ip: 192.168.86.194
this port:80 is on
this port:3306 is on
This scan spent 9.01316308975

"""
