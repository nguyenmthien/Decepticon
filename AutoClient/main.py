from webclient import getPacket
from tcpClient import sendMessage
from tcpClient import connect
from pathfinding import get_path
from translate_to_message import convert_to_message
from find_object import find_object
from find_object import come_to_object
from vertexChoose import verticesChoose

if __name__ == '__main__':
    
    team = input('What is your team? ')
    vertices = {}
    connect('192.168.137.128', 23)


    while True:
        getPacket(team)
        objects = find_object(1)
        if (come_to_object(objects)):
            termination = vertices['ourGoal']
        else:
            termination = verticesChoose(objects)
            
        path = get_path(('auto_ally', 'vertex1'), termination)
        word = convert_to_message(('auto_ally', 'vertex1'), path[1])
        sendMessage(word)