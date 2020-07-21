#!/usr/bin/python3.6
import requests
import pprint

res = requests.get('http://192.168.1.143/index.php/RestAPI/BasicBox/BoxMesApi')

pprint.pprint(res.json())
