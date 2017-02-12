# -*- coding: utf-8 -*-
import socket
import sys
from _thread import *

import argparse

parser = argparse.ArgumentParser(description="verbindet dich mit einem p2p chat.")
parser.add_argument("ip", type=int,
                    help="bootstrap IP")
parser.add_argument("port", type=int,
                    help="bootstrap port")


args = parser.parse_args()



#just testing - ignore
def threaded_client(conn):
    conn.send('Hello World!\n')

    while True:
        data = conn.recv(1024)
        reply = "nice to see you: " + data
        if not data:
            break
        conn.sendall(reply)



host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print (str(e))

s.listen(5)

print 'waiting for incoming connections...'


server = 'google.com'
server_ip = socket.gethostbyaddr(server)
print server_ip

while True:
    conn, addr = s.accept()
    print ('connected to: ' + addr[0]+ ':' + str(addr[1]))

    start_new_thread(threaded_client,(conn,))


