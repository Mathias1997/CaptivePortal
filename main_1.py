__author__ = "Ib Helmer Nielsen"
__copyright__ = "Copyright 2024, IT-Tek"
__credits__ = ["DonskyTech"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "IHN"
__email__ = "ihn@ihn.dk"
__status__ = "Development"
from machine import Pin, I2C  # ESP32 hardware
import ssd1306				  # OLED driver
import time					  # Time lib
import network				  # Network lib

# init OLED
# using default address 0x3C
#i2c = I2C(sda=Pin(4), scl=Pin(5))
n = network.WLAN(network.STA_IF)

i2c = I2C(1, scl = Pin(22), sda = Pin(21), freq = 400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.text('AP Oprettet',0,0,1)
display.text('SSID:'+SSID,0,10,1)
display.text('PW:'+PW ,0,20,1)
display.text('ip:'+ap.ifconfig()[0],0,30,1)
display.text('Gruppe4', 0, 40, 1)
if n.isconnected():
    display.text('Connected to network',0,50,1)

display.show()

while True:
    time.sleep(5)
