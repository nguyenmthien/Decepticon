#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Khai báo các thư viện được sử dụng
import websocket
import json
import ssl
import time
import urllib.request
import math
import numpy as np
from collections import defaultdict

from pathlib import Path


## Cài đặt và trả về thông tin cho giao thức mã hoá HTTPS
def makeSSLContext(ca, crt, key):
    sslCTX = ssl.create_default_context(
        purpose=ssl.Purpose.SERVER_AUTH,
        cafile=ca
    )

    sslCTX.load_cert_chain(crt, key)

    return sslCTX


## Trả về chuỗi JSON chứa thông tin đăng nhâp
def makeJSONCredentials(username, password):
    creds = {
        "username": username,
        "password": password
    }

    return json.dumps(creds).encode("utf-8")


## Cài đặt và trả về thông tin của yêu cầu HTTPS
def makeRequestHeader(url, contentType, content):
    req = urllib.request.Request(url)

    req.add_header('Content-Type', contentType)
    req.add_header('Content-Length', len(content))

    return req


## Gửi yêu cầu đăng nhập và trả về mã xác thực
def getToken(url, username, password,
             ca, crt, key):
    reqSSLContext = makeSSLContext(ca, crt, key)
    reqContent = makeJSONCredentials(username, password)
    req = makeRequestHeader(
        url,
        'application/json; charset=utf-8',
        reqContent
    )

    # Gửi yêu cầu và nhận kết quả trả về
    resp = urllib.request.urlopen(
        req, data=reqContent, context=reqSSLContext)

    # Đọc và trả về mã xác thực
    respBody = resp.read()
    respBodyJSON = json.loads(respBody.decode('utf-8'))

    return respBodyJSON["token"]


# Đăng nhập và nhận dữ liệu


## Cài đặt thông tin của giao thức mã hoá cho Websocket

# Đường dẫn đến các tập tin nhận từ BTC
CA_CRT = str(Path("cacert.pem"))
CRT = str(Path("clientcert.pem"))
KEY = str(Path("clientkey.pem"))

sslopt = {
    'cert_reqs': ssl.PROTOCOL_SSLv23,
    'keyfile': KEY,
    'certfile': CRT,
    'ca_certs': CA_CRT,
}


## Nhận mã xác thực và thêm mã xác thực vào thông tin yêu cầu Websocket

# Tên địa chỉ server (thay đổi vào ngày thi đấu)
HOST = "test.tunglevo.com"
# Tên cổng kết nối (thay đổi vào ngày thi đấu)
PORT = 4433

url = 'https://%s:%s/subscribe' % (HOST, PORT)
token = getToken(url,
                 # Thông tin tài khoản của mỗi đội
                 'user', 'password',
                 CA_CRT, CRT, KEY)

header = {
    'Authorization': 'Bearer %s' % (token)
}


## Thiết lập kết nối Websocket và bắt đầu nhận dữ liệu
url = 'wss://%s:%s/data' % (HOST, PORT)
ws = websocket.create_connection(url,
                                 header=header,
                                 sslopt=sslopt)

# x axis
v2 = np.array([1,0])

#Hàm tìm góc giữa trục x và vecto (từ điểm đến [0,0])
#Angle is in degree
def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


while True:
    msg = ws.recv()
    packet = json.loads(msg.decode('utf-8'))

    for i in range (0, 28):
        #print (packet['data'][i]["position"])
        #print (angle(packet['data'][i]["position"], v2))
        packet['data'][i].update({'angle' : angle(packet['data'][i]["position"], v2)})
        # nested dictionary

    # Hình hộp
    for j in range (4, 11):
        packet['data'][j].update({'point' : 5})

    # Hình dẹt
    for k in range (11, 15):
        packet['data'][k].update({'point' : 10})

    # Hình dĩa
    for r in range (15, 18):
        packet['data'][r].update({'point' : 15})

    # Hình máy bay
    for o in range (18, 20):
        packet['data'][o].update({'point' : 20})

    # Hình cái bàn
    for w in range (20, 22):
        packet['data'][w].update({'point' : 25})

    # Hình phi tiêu
    for l in range (22, 24):
        packet['data'][l].update({'point' : 30})

    # Bom
    for n in range (24, 25):
        packet['data'][n].update({'point' : -20})

    #File.truncate(0) #add this to delete all content in text file

    #input to text file
    File = open("coordinate.txt", "w+")
    string = str(packet)
    File.writelines(string+ '\n')

    print(packet)
    
    time.sleep(1)
    ws.send(json.dumps({'finished': True}).encode('utf-8'))

    

