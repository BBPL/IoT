# boot.py -- run on boot-up
from network import WLAN
import pycom


pycom.heartbeat(False)
pycom.rgbled(0x00ff00)

wlan = WLAN()