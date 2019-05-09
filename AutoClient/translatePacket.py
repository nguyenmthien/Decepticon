import numpy as np
import math
import calculatePacket as cal
import client+WritePacket as main


if __name__ == "__main__":
# x axis
v2 = np.array([1,0])

#Hàm tìm góc giữa trục x và vecto (từ điểm đến [0,0])
#Angle is in rad
    def dotproduct(v1, v2):
        return sum((a*b) for a, b in zip(v1, v2))

    def length(v):
        return math.sqrt(dotproduct(v, v))

    def angle(v1, v2):
        return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

# shifting the origin from top left to bot left 
    def newCoord(xorg, yorg):
        x = xorg
        y = -yorg +300
        return x, y

else:
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

    for n in range (0,28):          #position update with newCoord
        packet['data'][n].update({'position': newCoord(packet['data'][n]['position'][0], packet['data'][n]['position'][1])})

    for g in range (0, 28):
        packet['data'][g].update({'angle' : cal.angle(packet['data'][g]["dimension"], v2)})  #angle rad update
        # nested dictionary
