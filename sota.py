#! /usr/bin/ python3

import json
import requests
import subprocess
import time

url = "https://api2.sota.org.uk/api/spots/1/all"
RemoteCommand = "/usr/local/bin/RemoteCommand"
port = "7642"
page = "page"
ric = "0000056"

response = requests.get(url)
data = json.loads(response.text)

id = data[0]["id"]
activatorCallsign = data[0]["activatorCallsign"]
frequency = data[0]["frequency"]
mode = data[0]["mode"]
summitCode = data[0]["summitCode"]

while True:
    response = requests.get(url)
    data = json.loads(response.text)
    if data[0]["id"]==id:
         pass
    else:
         # Update the variables
         id = data[0]["id"]
         activatorCallsign = data[0]["activatorCallsign"]
         frequency = data[0]["frequency"]
         mode = data[0]["mode"]
         summitCode = data[0]["summitCode"]
         subprocess.call([RemoteCommand, port, page, ric, activatorCallsign, frequency, mode, summitCode])
    time.sleep(120)
