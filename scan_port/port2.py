#!/usr/bin/python

import sys
from  socket import *

#port2.py <host> <start_port>-<end>

host = sys.argv[1]
ports = sys.argv[2].split('-')

start_port = int(ports[0])
end_port = int(ports[1])

target_ip = gethostbyname(host)
opened_ports = []

for port in range(start_port,end_port+1):
    sock = socket()
    sock.settimeout(10)
    result = sock.connect_ex((target_ip,port))
    if result == 0:
        opened_ports.append(port)

print("opened ports:")
for i in opened_ports:
    print i
i
