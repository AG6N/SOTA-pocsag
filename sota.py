#! /usr/bin/ python3

import json
import requests
import subprocess
import time

url = "https://api2.sota.org.uk/api/spots/1/all"

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
        subprocess.call(["echo","1234 page 1234567 " +" ".join([activatorCallsign,frequency,mode,summitCode])])
    id = data[0]["id"]
    time.sleep(15)
