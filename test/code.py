from network import WLAN
import socket
import machine

def connect(wlan):
    
    if wlan.isconnected():
        client = socket.socket()
        address = "localhost"
        port = 5000
        ai = socket.getaddrinfo(address, port)
        print("Address infos:", ai)
        addr = ai[0][-1]
        print("Connect address:", addr)
        client.connect(addr)

        if False:
            # MicroPython socket objects support stream (aka file) interface
            # directly, but the line below is needed for CPython.
            client = client.makefile("rwb", 0)
            client.write(b"GET /home/h HTTP/1.0\r\n\r\n")
            print(client.read())
        else:
            client.send(b"GET /home/h HTTP/1.0\r\n\r\n")
            print(client.recv(4096))

        client.close()