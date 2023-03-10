#! /usr/bin/ python3

import json
import requests
import subprocess
import time
import pprint
import websocket

from websocket import create_connection
websocket.enableTrace(True)

url = "https://api2.sota.org.uk/api/spots/1/all"

response = requests.get(url)
data = json.loads(response.text)
id = data[0]["id"]

while True:
    response = requests.get(url)
    data = json.loads(response.text)
    if data[0]["id"]==id:
         pass
    else:
         id = data[0]["id"]
         activatorCallsign = data[0]["activatorCallsign"]
         frequency = data[0]["frequency"]
         mode = data[0]["mode"]
         associationCode = data[0]["associationCode"]
         summitCode = data[0]["summitCode"]
         ws = create_connection('ws://localhost:8055/')
         m_type = "AlphaNum"
         m_func = "Func3"
         ric = "56"
         text = (activatorCallsign+" "+frequency+" "+mode+" "+associationCode+"/"+summitCode)
         string_to_send = "{\"SendMessage\": {\"addr\": %s, \"data\": \"%s\", \"mtype\": \"%s\", \"func\": \"%s\"}}" % (ric, text, m_type, m_func)
         print(string_to_send)
         ws.send(string_to_send)

    time.sleep(60)
