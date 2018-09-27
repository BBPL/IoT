from network import WLAN
import socket
import machine
import os
import urequests

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
        print("entering request area")
        r = urequests.post("http://"+ip+":"+str(port)+"/connect", json = {"mit": "data"})
        print(r)
        print(r.content)
        print(r.text)
        print(r.content)
        print(r.json())

        # It's mandatory to close response objects as soon as you finished
        # working with them. On MicroPython platforms without full-fledged
        # OS, not doing so may lead to resource leaks and malfunction.
        r.close()
    print("exiting connect")
        
def testcon():
    a = os.system("ping -c 1 192.168.0.55:8000")
    print(a)

