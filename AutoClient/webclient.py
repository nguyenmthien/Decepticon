#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Góc được tính theo độ so với trục Ox

## Khai báo các thư viện được sử dụng
import websocket
import json
import ssl
import time
import urllib.request
import math
import numpy as np

from vertex import vertex
from vertex import rotate
from vertex import vertexNonBalance

from calculatePacket import dotproduct
from calculatePacket import length
from calculatePacket import angle
from calculatePacket import newCoord

from collections import defaultdict

from pathlib import Path

####################################################################### I didn't write this
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

###################################################################### I didn't write this

# x axis
v2 = np.array([1,0])

# Create a new dictionary that stores vertices of objects
vertices = dict();
vertices['manual_ally'] = {}
vertices['auto_ally'] = {}
vertices['manual_enemy'] = {}
vertices['auto_enemy'] = {}
vertices['cube1'] = {}
vertices['cube2'] = {}
vertices['cube3'] = {}
vertices['cube4'] = {}
vertices['cube5'] = {}
vertices['cube6'] = {}
vertices['cube7'] = {}
vertices['flat1'] = {}
vertices['flat2'] = {}
vertices['flat3'] = {}                      #case1 the origin is in bot left 
vertices['flat4'] = {}
vertices['disk1'] = {}
vertices['disk2'] = {}
vertices['disk3'] = {}
vertices['paper1'] = {}
vertices['paper2'] = {}
vertices['table1'] = {}
vertices['table2'] = {}
vertices['shuriken1'] = {}
vertices['shuriken2'] = {}
vertices['bomb'] = {}
vertices['ourGoal'] = {'vertex1': (135, 25)}   
vertices['theirGoal'] = {'vertex1': (175,275)}
vertices['ArenaVertices'] = {'vertex1': (25,275), 'vertex2': (275,275), 'vertex3': (275,25), 'vertex4': (25,25)}
vertices['ourWall'] = {'vertex1' : (110,0), 'vertex2': (110,25)}  #vertex1 is the bottom of the wall
vertices['theirWall'] = {'vertex1': (190, 300), 'vertex2': (190, 275)} #vertex2 is the top point of the wall

def getPacket(yourTeam):
    msg = ws.recv()
    global packet
    packet = json.loads(msg.decode('utf-8'))

    print(packet)
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
    for i in range (24, 25):
        packet['data'][i].update({'point' : -20})

    for n in range (0,28):
        if (packet['data'][n]['position'][0] > 0) & (packet['data'][n]['position'][1] > 0) & (yourTeam == '1') :
            packet['data'][n].update({'position': newCoord(packet['data'][n]['position'][0], packet['data'][n]['position'][1])})
        else:
            break
        
    for g in range (0, 28):
        packet['data'][g].update({'angle' : angle(packet['data'][g]["dimension"], v2)})  #angle rad update
        # nested dictionary
        
    vertices.update({'manual_ally': vertex(packet['data'][0]['position'][0],packet['data'][0]['position'][1], 20, packet['data'][0]['angle'])})
    vertices.update({'auto_ally': vertex(packet['data'][1]['position'][0],packet['data'][1]['position'][1], 20, packet['data'][1]['angle'])})
    vertices.update({'manual_enemy': vertex(packet['data'][2]['position'][0],packet['data'][2]['position'][1], 20, packet['data'][2]['angle'])})
    vertices.update({'auto_enemy': vertex(packet['data'][3]['position'][0],packet['data'][3]['position'][1], 20, packet['data'][3]['angle'])})

    vertices.update({'cube1': vertex(packet['data'][4]['position'][0],packet['data'][4]['position'][1], 8, packet['data'][4]['angle'])})
    vertices.update({'cube2': vertex(packet['data'][5]['position'][0],packet['data'][5]['position'][1], 8, packet['data'][5]['angle'])})
    vertices.update({'cube3': vertex(packet['data'][6]['position'][0],packet['data'][6]['position'][1], 8, packet['data'][6]['angle'])})
    vertices.update({'cube4': vertex(packet['data'][7]['position'][0],packet['data'][7]['position'][1], 8, packet['data'][7]['angle'])})
    vertices.update({'cube5': vertex(packet['data'][8]['position'][0],packet['data'][8]['position'][1], 8, packet['data'][8]['angle'])})
    vertices.update({'cube6': vertex(packet['data'][9]['position'][0],packet['data'][9]['position'][1], 8, packet['data'][9]['angle'])})
    vertices.update({'cube7': vertex(packet['data'][10]['position'][0],packet['data'][10]['position'][1], 8, packet['data'][10]['angle'])})

    vertices.update({'flat1': vertexNonBalance(packet['data'][11]['position'][0],packet['data'][11]['position'][1], 14, 8, packet['data'][11]['angle'])})
    vertices.update({'flat2': vertexNonBalance(packet['data'][12]['position'][0],packet['data'][12]['position'][1], 14, 8, packet['data'][12]['angle'])})
    vertices.update({'flat3': vertexNonBalance(packet['data'][13]['position'][0],packet['data'][13]['position'][1], 14, 8, packet['data'][13]['angle'])})
    vertices.update({'flat4': vertexNonBalance(packet['data'][14]['position'][0],packet['data'][14]['position'][1], 14, 8, packet['data'][14]['angle'])})

    vertices.update({'disk1': vertex(packet['data'][15]['position'][0],packet['data'][15]['position'][1], 15 ,packet['data'][15]['angle'])})
    vertices.update({'disk2': vertex(packet['data'][16]['position'][0],packet['data'][16]['position'][1], 15 ,packet['data'][16]['angle'])})
    vertices.update({'disk3': vertex(packet['data'][17]['position'][0],packet['data'][17]['position'][1], 15 ,packet['data'][17]['angle'])})

    vertices.update({'paper1': vertexNonBalance(packet['data'][18]['position'][0],packet['data'][18]['position'][1], 20, 15, packet['data'][18]['angle'])})
    vertices.update({'paper2': vertexNonBalance(packet['data'][19]['position'][0],packet['data'][19]['position'][1], 20, 15, packet['data'][19]['angle'])})

    vertices.update({'table1': vertexNonBalance(packet['data'][20]['position'][0],packet['data'][20]['position'][1], 20, 10, packet['data'][20]['angle'])})
    vertices.update({'table2': vertexNonBalance(packet['data'][21]['position'][0],packet['data'][21]['position'][1], 20, 10, packet['data'][21]['angle'])})

    vertices.update({'shuriken1': vertex(packet['data'][22]['position'][0],packet['data'][22]['position'][1], 12.8, packet['data'][22]['angle'])})
    vertices.update({'shuriken2': vertex(packet['data'][23]['position'][0],packet['data'][23]['position'][1], 12.8, packet['data'][23]['angle'])})

    vertices.update({'bomb': vertexNonBalance(packet['data'][24]['position'][0],packet['data'][24]['position'][1], 16, 14.4, packet['data'][24]['angle'])})
    '''
    for x in vertices.keys():
        #print( x, ': ', vertices[x])
        for i in vertices[x].keys():
            #print(i, ": ", vertices[x][i])
            if vertices[x][i][0] < 0 && vertices[x][i][1] > 0:
    '''
    
    
    #print(vertices['manual_ally']['vertex0'][0])
    #print(vertices)
    
    time.sleep(1)
    #ws.send(json.dumps({'finished': True}).encode('utf-8'))

if __name__ == "__main__":
    Team = input("enter your team: ")
    #print(type(Team))
    while True:
        getPacket(Team)
        print(packet)
        print(vertices)
        #print(vertices.keys())  #accessing vertices' keys
        
