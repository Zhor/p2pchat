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
port = args.port
ip = args.ip

#Nachbarliste
listOfH = []



# todo:
# verbinden mit übergebener IP
# joinnachrichten senden, um netz zu erkunden und x=3? nachbarn zu finden
# (joinantworten auswerten)
# nachricht senden = fluten
# nachricht erhalten & weiterleiten


firstsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
firstsocket.bind((ip, port))

#Nachricht senden
def sendMessage(self, message):
    totalsent = 0
    MSGLEN = len(message)
    while totalsent < MSGLEN:
        sent = self.sock.send(message[totalsent:])
        if sent == 0:
            raise RuntimeError("Fehler")
        totalsent = totalsent + sent


#Nachricht empfangen
def receiveMessage(self):
    chunks = []
    bytes_recd = 0
    while bytes_recd < MSGLEN:
        chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
        if chunk == '':
            raise RuntimeError("Fehler")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return ''.join(chunks)

#erhalten Nachrichten weiterleiten
def reSendMessage(self, message):
    for i in listOfH:
        threaded_client()

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


