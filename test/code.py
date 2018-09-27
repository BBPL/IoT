from network import WLAN
import socket
import machine
import os

wlan = WLAN(mode=WLAN.STA)

def wifiSetup(name,pwd):
    
    nets = wlan.scan()

    for net in nets:
        print(net.ssid)
        if net.ssid == name:
            print('Network found!')
            wlan.connect(net.ssid, auth=(net.sec, pwd), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print('WLAN connection succeeded!')
            break

def connect(ip = "192.168.0.55",port =80):
    
    if wlan.isconnected():
        client = socket.socket()
        address = ip
        ai = socket.getaddrinfo(ip, port)
        print("Address infos:", ai)
        addr = ai[0][-1]
        print("Connect address:", addr)
        
        client.connect(addr)
        
        client.send(b"POST /home/h HTTP/1.0\r\n\r\n")
        print(client.recv(4096))

        # if False:
        #     # MicroPython socket objects support stream (aka file) interface
        #     # directly, but the line below is needed for CPython.
        #     client = client.makefile("rwb", 0)
        #     client.write(b"GET /home/h HTTP/1.0\r\n\r\n")
        #     print(client.read())
        # else:
        #     client.send(b"GET / HTTP/1.0\r\n\r\n")
        #     print(client.recv(4096))

        client.close()

def testcon():
    a = os.system("ping -c 1 192.168.0.55:8000")
    print(a)

