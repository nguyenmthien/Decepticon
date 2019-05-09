import astar
import os
import sys
import math


class Station:

    def __init__(self, id, name, position):
        self.id = id
        self.name = name
        self.position = position
        self.links = []



def get_path(s1, s2):
    """ runs astar on the map"""
    def ccw(A,B,C):
	    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

    def intersect(A,B,C,D):
	    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
    
    def distance(n1, n2):
        # n1, n2 co dang ('manual_ally', 'vertex1')
        """computes the distance between two vertices"""
        if (n1[1] == 'vertex0' or n2[1] == 'vertex0'):
            return 30041975
        x1, y1 = vertices[n1[0]][n1[1]]
        x2, y2 = vertices[n2[0]][n2[1]]
        for objects in vertices:
            if (objects == 'ourWall' or objects == 'theirWall'):
                vertex1 = vertices[objects]['vertex1']
                vertex2 = vertices[objects]['vertex2']
                if (intersect((x1, y1), (x2, y2), vertex1, vertex2)):
                    return 30041975

            if (len(vertices[objects]) == 5):
                vertex1 = vertices[objects]['vertex1']
                vertex2 = vertices[objects]['vertex2']
                vertex3 = vertices[objects]['vertex3']
                vertex4 = vertices[objects]['vertex4']
                
                in13 = intersect((x1, y1), (x2, y2), vertex1, vertex3)
                in24 = intersect((x1, y1), (x2, y2), vertex2, vertex4)
                if (in13 or in24):
                    return 30041975

        
        return (x1 - x2)**2 + (y1 - y2)**2
    
    def neighbor(node):
        s = []
        for objects in vertices:
            for vertex in vertices[objects]:
                s.append((objects, vertex))
        return s

    return astar.find_path(s1, s2, neighbors_fnct=neighbor, heuristic_cost_estimate_fnct=distance, distance_between_fnct=distance)


if __name__ == '__main__':

    vertices = {'manual_ally': {'vertex0': (556, -733), 'vertex1': (556, -728.5), 'vertex2': (560.5, -733), 'vertex3': (556, -737.5), 'vertex4': (551.5, -733)}, 'auto_ally': {'vertex0': (1329, -519), 'vertex1': (1329, -514.5), 'vertex2': (1333.5, -519), 'vertex3': (1329, -523.5), 'vertex4': (1324.5, -519)}, 'manual_enemy': {'vertex0': (466, -795), 'vertex1': (466, -790.5), 'vertex2': (470.5, -795), 'vertex3': (466, -799.5), 'vertex4': (461.5, -795)}, 'auto_enemy': {'vertex0': (240, -217), 'vertex1': (240, -212.5), 'vertex2': (244.5, -217), 'vertex3': (240, -221.5), 'vertex4': (235.5, -217)}, 'cube1': {'vertex0': (1304, -270), 'vertex1': (1304, -265.5), 'vertex2': (1308.5, -270), 'vertex3': (1304, -274.5), 'vertex4': (1299.5, -270)}, 'cube2': {'vertex0': (592, -802), 'vertex1': (592, -797.5), 'vertex2': (596.5, -802), 'vertex3': (592, -806.5), 'vertex4': (587.5, -802)}, 'cube3': {'vertex0': (724, -20), 'vertex1': (724, -15.5), 'vertex2': (728.5, -20), 'vertex3': (724, -24.5), 'vertex4': (719.5, -20)}, 'cube4': {'vertex0': (1488, -936), 'vertex1': (1488, -931.5), 'vertex2': (1492.5, -936), 'vertex3': (1488, -940.5), 'vertex4': (1483.5, -936)}, 'cube5': {'vertex0': (968, -440), 'vertex1': (968, -435.5), 'vertex2': (972.5, -440), 'vertex3': (968, -444.5), 'vertex4': (963.5, -440)}, 'cube6': {'vertex0': (1477, -509), 'vertex1': (1477, -504.5), 'vertex2': (1481.5, -509), 'vertex3': (1477, -513.5), 'vertex4': (1472.5, -509)}, 'cube7': {'vertex0': (1117, -534), 'vertex1': (1117, -529.5), 'vertex2': (1121.5, -534), 'vertex3': (1117, -538.5), 'vertex4': (1112.5, -534)}, 'flat1': {'vertex0': (805, -650), 'vertex1': (805, -645.5), 'vertex2': (809.5, -650), 'vertex3': (805, -654.5), 'vertex4': (800.5, -650)}, 'flat2': {'vertex0': (349, 243), 'vertex1': (349, 247.5), 'vertex2': (353.5, 243), 'vertex3': (349, 238.5), 'vertex4': (344.5, 243)}, 'flat3': {'vertex0': (1234, -542), 'vertex1': (1234, -537.5), 'vertex2': (1238.5, -542), 'vertex3': (1234, -546.5), 'vertex4': (1229.5, -542)}, 'flat4': {'vertex0': (555, -801), 'vertex1': (555, -796.5), 'vertex2': (559.5, -801), 'vertex3': (555, -805.5), 'vertex4': (550.5, -801)}, 'disk1': {'vertex0': (592, 138), 'vertex1': (592, 142.5), 'vertex2': (596.5, 138), 'vertex3': (592, 133.5), 'vertex4': (587.5, 138)}, 'disk2': {'vertex0': (567, -139), 'vertex1': (567, -134.5), 'vertex2': (571.5, -139), 'vertex3': (567, -143.5), 'vertex4': (562.5, -139)}, 'disk3': {'vertex0': (221, -565), 'vertex1': (221, -560.5), 'vertex2': (225.5, -565), 'vertex3': (221, -569.5), 'vertex4': (216.5, -565)}, 'paper1': {'vertex0': (631, -415), 'vertex1': (631, -410.5), 'vertex2': (635.5, -415), 'vertex3': (631, -419.5), 'vertex4': (626.5, -415)}, 'paper2': {'vertex0': (353, -530), 'vertex1': (353, -525.5), 'vertex2': (357.5, -530), 'vertex3': (353, -534.5), 'vertex4': (348.5, -530)}, 'table1': {'vertex0': (731, -241), 'vertex1': (731, -236.5), 'vertex2': (735.5, -241), 'vertex3': (731, -245.5), 'vertex4': (726.5, -241)}, 'table2': {'vertex0': (1187, -443), 'vertex1': (1187, -438.5), 'vertex2': (1191.5, -443), 'vertex3': (1187, -447.5), 'vertex4': (1182.5, -443)}, 'shuriken1': {'vertex0': (164, -1139), 'vertex1': (164, -1134.5), 'vertex2': (168.5, -1139), 'vertex3': (164, -1143.5), 'vertex4': (159.5, -1139)}, 'shuriken2': {}, 'bomb': {'vertex0': (150, 33), 'vertex1': (150, 37.5), 'vertex2': (154.5, 33), 'vertex3': (150, 28.5), 'vertex4': (145.5, 33)}}

    path = get_path(('manual_ally', 'vertex2'), ('cube1', 'vertex4'))

    for v in path:
        print(v)

