import math

def rotate(xor, yor, px, py, angle):
    radius = math.sqrt((px-xor)**2 + (py-yor)**2)
    x = xor + math.cos(angle) * radius
    y = yor + math.sin(angle) * radius
    return x, y      

def vertex(x, y, L, phi): #only for cubes, disks and vehicles
    offset = 0.5             # this will be adjust later
    vertex = dict();
    vertex['vertex0'] = x, y 
            
    x1 = x                      # L is the length of the square edge 
    y1 = y + offset + L/2            # phi is the rotation angle
    rotate(x, y, x1, y1, phi)
    vertex['vertex1'] = x1, y1
            
    x2 = x+ offset + L/2
    y2 = y
    rotate(x, y, x2, y2, phi)
    vertex['vertex2'] = x2, y2
            
    x3 = x
    y3 = y - offset - L/2
    rotate(x, y, x3, y3, phi)
    vertex['vertex3'] = x3, y3

    x4 = x - offset - L/2
    y4 = y
    rotate(x, y, x4, y4, phi)
    vertex['vertex4'] = x4, y4

    return vertex

def vertexNonBalance(x, y, L, W, phi):      #for others objects
    offset = 0.5
    vertexNonBalance = dict();
    vertexNonBalance['vertex0'] = x, y

    x1 = x
    y1 = y + W/2 + offset
    rotate(x, y, x1, y1, phi)
    vertexNonBalance['vertex1'] = x1, y1

    x2 = x + offset + L/2
    y2 = y
    rotate(x, y, x2, y2, phi)
    vertexNonBalance['vertex2'] = x2, y2

    x3 = x 
    y3 = y - W/2 - offset
    rotate(x, y, x3, y3, phi)
    vertexNonBalance['vertex3'] = x3, y3

    x4 = x - L/2 -offset
    y4 = y
    rotate(x, y, x4, y4, phi)
    vertexNonBalance['vertex4'] = x4, y4

    return vertexNonBalance
#d = vertex(data[0]['position'][0], data[0]['position'][1], 8, 30)
#print(vertex(data[0]['position'][0], data[0]['position'][1], 8, 30))
#print(rotate(d['vertex0'][0], d['vertex0'][1], d['vertex1'][0], d['vertex1'][1], (math.pi)/2))
#print(data[0]['position'][0])
'''
def verticesUpdate(packet):
    vertices.update({'manual_ally': vertex(packet['data'][0]['position'][0],packet['data'][0]['position'][1], 20, packet['data'][0]['angle'])})
    vertices.update({'auto_ally': vertex(packet['data'][1]['position'][0],packet['data'][1]['position'][1], 20, packet['data'][1]['angle'])})
    vertices.update({'manual_enemy': (packet['data'][2]['position'][0],packet['data'][2]['position'][1], 20, packet['data'][2]['angle'])})
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
#print (vertices['manual_ally']['vertex3']) #accessing element in vertex
'''
