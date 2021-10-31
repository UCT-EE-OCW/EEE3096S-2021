import socket
import sys

f = open("/data/sensorlog.txt", "w+")











#TODO: Add code to create a socket ready to recieve data
















with newconnection:
    while True:
        data = newconnection.recv(1024)
        print('\nReceived', repr(data))
        f.write("\nReceived: ")
        f.write(repr(data))
        f.flush()
        if not data: break


