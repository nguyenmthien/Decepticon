

#Criteria is 1 to find nearest object

def find_object(criteria):
    if criteria == 1:
        min_distance = 30041975
        object_name = 'auto_ally'
        x0, y0 = (0, 0)
        x, y = (0, 0)
        for objects in packet['data']:
            if objects['name'] == 'auto_ally':
                x0, y0 = objects['position']
        for objects in packet['data']:
            x, y = objects['position']
            distance = abs(x - x0) + abs(y - y0)
            if ((distance < min_distance) and (objects['name'] != 'auto_ally')):
                min_distance = distance
                object_name = objects['name']
        return object_name

def come_to_object(object_name):
    x0, y0 = (0, 0)
    x, y = (0, 0)
    for objects in packet['data']:
        if objects['name'] == 'auto_ally':
            x0, y0 = objects['position']
    for objects in packet['data']:
        if objects['name'] == object_name:
            x, y = objects['position']
    if ((x-x0)**2+(y-y0)**2 < 400.0):
        return True
    return False



if __name__ == '__main__':
    packet = {'time': 1557066369263932504, 'data': [{'dimension': [33, 53], 'name': 'manual_ally', 'position': [33, 53], 'angle': 1.164996770243548}, {'dimension': [-18, -76], 'name': 'auto_ally', 'position': [34, 54], 'angle': 0.6487812709306812}, {'dimension': [-69, -78], 'name': 'manual_2', 'position': [45, 658], 'angle': 1.5025135908212544}, {'dimension': [67, -45], 'name': 'auto_enemy', 'position': [769, 1125], 'angle': 0.9711923711730313}, {'dimension': [84, 76], 'name': 'object_1', 'position': [32, 627], 'angle': 1.519803887534408, 'point': 5}, {'dimension': [39, -87], 'name': 'object_2', 'position': [427, 707], 'angle': 1.0274698579685673, 'point': 5}, {'dimension': [-25, -47], 'name': 'object_3', 'position': [1364, 402], 'angle': 0.28660704131091447, 'point': 5}, {'dimension': [37, -36], 'name': 'object_4', 'position': [159, 217], 'angle': 0.9384471720272266, 'point': 5}, {'dimension': [-31, 74], 'name': 'object_5', 'position': [1106, 183], 'angle': 0.163975485402652, 'point': 5}, {'dimension': [-47, 30], 'name': 'object_6', 'position': [1171, 246], 'angle': 0.20706580421756143, 'point': 5}, {'dimension': [68, 49], 'name': 'object_7', 'position': [1378, 1409], 'angle': 0.7965207761089004, 'point': 5}, {'dimension': [22, 32], 'name': 'object_8', 'position': [896, 443], 'angle': 0.4591733659267985, 'point': 10}, {'dimension': [-14, 20], 'name': 'object_9', 'position': [446, 1338], 'angle': 1.2490457723982544, 'point': 10}, {'dimension': [-65, 1], 'name': 'object_10', 'position': [12, 564], 'angle': 1.5495229407708355, 'point': 10}, {'dimension': [-12, 39], 'name': 'object_11', 'position': [670, 1267], 'angle': 1.0843686390743261, 'point': 10}, {'dimension': [53, -21], 'name': 'object_12', 'position': [136, 84], 'angle': 0.5532943253222926, 'point': 15}, {'dimension': [29, 57], 'name': 'object_13', 'position': [481, 464], 'angle': 0.7674106856047571, 'point': 15}, {'dimension': [-29, -90], 'name': 'object_14', 'position': [578, 1392], 'angle': 1.1772300712371, 'point': 15}, {'dimension': [86, -9], 'name': 'object_15', 'position': [556, 1354], 'angle': 1.1811554663714416, 'point': 20}, {'dimension': [-51, -28], 'name': 'object_16', 'position': [1266, 1453], 'angle': 0.8540653185259368, 'point': 20}, {'dimension': [-82, -85], 'name': 'object_17', 'position': [306, 234], 'angle': 0.6528466311007745, 'point': 25}, {'dimension': [90, -10], 'name': 'object_18', 'position': [1089, 329], 'angle': 0.2933933080123741, 'point': 25}, {'dimension': [-5, -55], 'name': 'object_19', 'position': [1381, 1405], 'angle': 0.7940124513907728, 'point': 30}, {'dimension': [-37, 46], 'name': 'object_20', 'position': [374, 1021], 'angle': 1.2196681342083513, 'point': 30}, {'dimension': [58, 1], 'name': 'object_21', 'position': [483, 1412], 'angle': 1.2412052888577487, 'point': -20}, {'dimension': [-57, 27], 'name': 'object_22', 'position': [351, 125], 'angle': 0.34212125064964055}, {'dimension': [-49, 42], 'name': 'object_23', 'position': [621, 279], 'angle': 0.42225115345127195}, {'dimension': [76, -86], 'name': 'object_24', 'position': [636, 727], 'angle': 0.8520637171223214}]}
    print(find_object(1))
    print(come_to_object('manual_ally'))

        