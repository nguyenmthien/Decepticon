import math
import numpy as np

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
