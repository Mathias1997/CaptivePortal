__author__ = "gruppe 4"
__copyright__ = "Copyright 2024, IT-Tek"
__credits__ = ["DonskyTech"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "IHN"
__email__ = "ihn@ihn.dk"
__status__ = "Development"
# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import os
esp.osdebug(None)
#import webrepl
#webrepl.start()

from machine import Pin, I2C  # ESP32 hardware
import utime                  # Time lib
import network                # Network lib

SSID = "IHP-AP-GR4"
PW = "MaaGodt*7913"
ap = network.WLAN(network.AP_IF)
def apMode():
     # Opretter en access point interface
    ap.active(True)                      # Aktiverer interface
    ap.config(essid=SSID, password=PW)   # Sætter SSID og adgangskode
    while ap.active() == False:          # Vent til ap aktiv
        pass
    print("Ap aktiv !!")                 # Debugging besked

def connectMode():
    ap.disconnect()
    n = network.WLAN(network.STA_IF)
    n.active(True)
    with open("credentials.txt",'r') as f:
        settings = [i.rstrip() for i in f]
    ssid = settings[0]
    password = settings[1]
    print(f"SSID: {ssid}, Password: {password}")
    n.connect(str(ssid),str(password))
    while not n.isconnected():
        pass
    print('network config:', n.ifconfig())

try:
    f = open('credentials.txt','r')
    print("credentials file exists")

except:
    apMode()

else:
    connectMode()
    
