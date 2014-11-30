#!/usr/bin/env python
__author__ = 'Loc Le'

import socket

TCP_IP = '192.168.56.1'
TCP_PORT = 5005
BUFFER_SIZE = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# This loop sends and receives messages between the client and server to play the game
# until the word "Winner" is found, which will break the loop and close the connection
while True:
    data = s.recv(BUFFER_SIZE)
    print "received data:", data
    var = raw_input()
    s.send(var)
    list1 = data.split()
    # Check to see if the first word is "Winner",
    # meaning someone won the game so it should break the loop and close the connection
    if list1[0] == "Winner":
        break

s.close()