#!/usr/bin/python

import sys
import threading
from socket import *

lock = threading.RLock()

def tcp_test(port):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip,port))
    if result == 0:
        lock.acquire()
        print "opened ports:",port
        lock.release()

if __name__ == '__main__':
    hosts = []
    ports = []
    with open('allhost.txt') as f:
        hosts.append(f.readline())

    with open('allports.txt') as f:
        ports.append(f.readline())
        

    for host in hosts:
        target_ip = gethostbyname(host)
        print target_ip

        for port in ports:
            port = int(port)
            #port = list(port)
            t = threading.Thread(target=tcp_test,args=(port,))
            t.start()

