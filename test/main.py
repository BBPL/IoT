# main.py -- put your code here!
# LIS2HH12.roll()
from network import WLAN
import socket
import machine
import code


wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()

for net in nets:
    print(net.ssid)
    if net.ssid == 'Majbrit':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'D3025d3025'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break

code.connect(wlan)




