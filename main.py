from machine import Pin, I2C  # ESP32 hardware
import ssd1306				  # OLED driver
import time					  # Time lib
import network				  # Network lib
from microdot import Microdot

# test
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

app = Microdot()

credentials_file_path = 'credentials.txt'

indexHtml = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Captive Portal Group 4</title>
</head>
<body>

    <h1>Captive Portal Group 4</h1>
    <br>
    <form action="Credentials" method="post">
        <p>Enter your SSID: </p>
        <input type="text" name="SSID">
        <br>
        <p>Enter your password</p>
        <input type="password" name="password">
        <br><br>
        <input type="submit" value="LOGIN" id="login">
    </form>
</body>
</html>
'''


@app.route('/')
async def index(request):
    print('Succesful')
    return indexHtml, 200, {'Content-Type': 'text/html'}

@app.route('/version')
async def version(request):
    return 'Version 0.5/UCN'

@app.route('/Credentials', methods=["POST", "GET"])
async def Connect(request):
    form_data = request.form
    ssid = form_data['SSID']
    password = form_data['password']
    with open(credentials_file_path,'w') as f:
        f.write(str(ssid)+'\n')
        f.write(str(password)+'\n')
    

if __name__ == '__main__':
    app.run(port=80)
