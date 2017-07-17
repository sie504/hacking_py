#!/usr/bin/python
import sys
import threading
from socket import *

lock = threading.RLock()

def tcp_test(port):
    sock =  socket(AF_INET,SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip,port))
    if result == 0:
        lock.acquire()
        print "opened ports:",port
        lock.release()

if __name__ == '__main__':
    host = sys.argv[1]
    ports = sys.argv[2].split('-')

    s_port = int(ports[0])
    e_port = int(ports[1])

    target_ip = gethostbyname(host)
    for port in range(s_port,e_port):
        t = threading.Thread(target=tcp_test,args=(port,))
        t.start()

