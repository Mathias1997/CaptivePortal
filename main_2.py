from microdot import Microdot


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
