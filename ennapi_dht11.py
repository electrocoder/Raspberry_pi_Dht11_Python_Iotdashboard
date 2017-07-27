# -*- coding: utf-8 -*-

"""
    Proje adi   :   EnnaSa
    Amac        :   Python ile IoThook REST Api Kullanarak Orange Pi Zero uzerinden Sicaklik ve Nem olcumlerinin yapilmasi
    Tarih       :   27 Temmuz 2017
    Yazan       :   Sahin MERSIN
    Web         :   http://www.iothook.com
    Yayin       :   http://mesebilisim.com
"""

import requests
import json
import urllib
import urllib2
import random
import pprint
import time

import RPi.GPIO as GPIO

import dht11
import datetime


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=02)

headers = {'Content-type': 'application/json'}
url = 'https://iothook.com/api/v1.2/datas/'

auth=('USERNAME', 'PASSWORD')

while True:
        try:
                result = instance.read()
                if result.is_valid():
                        print("Last valid input: " + str(datetime.datetime.now()))
                        print("Temperature: %d C" % result.temperature)
                        print("Humidity: %d %%" % result.humidity)

                        data={
                        'api_key':'CHANNEL_API_KEY',
                        'value_1':result.temperature,
                        'value_2':result.humidity,
                        }

                        data_json = json.dumps(data)
                        response = requests.post(url, data=data_json, headers=headers, auth=auth)
                        print(response)
                        print(response.json())
                        time.sleep(15)
                else:
                        print('dht11 hatasi')
                        time.sleep(3)
        except:
                print('internet baglanti hatasi')
                time.sleep(3)


