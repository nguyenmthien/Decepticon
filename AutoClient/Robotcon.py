def bubbleSort(array, indexArray_b, objectSocreRanking_b):
    for count in range(len(array)):
        for count_1 in range(len(array) - count - 1):
            if (array[count + count_1 + 1] < array[count]):
				#Sắp xếp theo khoảng cách
                temporary = array[count]
                array[count] = array[count + count_1 + 1]
                array[count + count_1 + 1] = temporary	 
				
				#Cập nhập điểm
                temporary = objectSocreRanking_b[count]
                objectSocreRanking_b[count] = objectSocreRanking_b[count + count_1 + 1]
                objectSocreRanking_b[count + count_1 + 1] = temporary
				
				#Cập nhập index
                temporary = indexArray_b[count]
                indexArray_b[count] = indexArray_b[count + count_1 + 1]
                indexArray_b[count + count_1 + 1] = temporary

"""
	Biến priority thể hiện sự ưu tiên trong chọn vật:
		0 : chọn vật ít điểm nhất trước
		1 : chọn vật nhiều điểm nhất trước
		2 : chọn vật gần nhất trước
	"""

def selectionTarget(priority):
	
    distanceArray = [100, 2, 1, 50, 45, 20, 18]
    indexArray = [1, 2, 3, 4, 5, 6, 7]
    scoreArray = [100, 50, 70, 10, 60, 40, 25]
    data = 7
    
    bubbleSort(distanceArray, indexArray, scoreArray)

    for count in range(data):
        if (distanceArray[count] != 0):
            scoreArray.append(count)
        else:
            scoreArray.append(100000000)
	
    if (priority == 0):
        selectionScoreMin = min(scoreArray)
        selectionIndex = 0
                
        for i in range(len(scoreArray)):
            if selectionScoreMin == scoreArray[i]:
                selectionIndex = indexArray[i]
        return 0
					
    if (priority == 1):
        selectionScoreMax = max(scoreArray)
        selectionIndex = 0

        for j in range(len(scoreArray)):
            if selectionScoreMax == scoreArray[j]:
                selectionIndex = indexArray[j]
        return 1                
					
    if (priority == 2):
        selectionDistance = min(distanceArray)
        selectionIndex = 0

        for k in range(len(distanceArray)):
            if selectionDistance == distanceArray[k]:
                selectionIndex = indexArray[k]
        return 2

if __name__=='__main__':
    data = {'time': 1557384366836128440, 'data': [{'dimension': [-13, 9], 'name': 'manual_1', 'position': (746, 155), 'angle': 2.5360479899848234}, {'dimension': [-2, -25], 'name': 'auto_1', 'position': (604, -72), 'angle': 1.6506263125071339}, {'dimension': [-66, -77], 'name': 'manual_2', 'position': (1458, -280), 'angle': 2.279422598922567}, {'dimension': [41, -25], 'name': 'auto_2', 'position': (386, 204), 'angle': 0.5475622359399975}, {'dimension': [-77, 12], 'name': 'object_1', 'position': (1118, 225), 'point': 5, 'angle': 2.986992108158593}, {'dimension': [73, -34], 'name': 'object_2', 'position': (409, -859), 'point': 5, 'angle': 0.4358769724073852}, {'dimension': [-52, -28], 'name': 'object_3', 'position': (846, 3), 'point': 5, 'angle': 2.647651284670212}, {'dimension': [33, -37], 'name': 'object_4', 'position': (686, 227), 'point': 5, 'angle': 0.8424789458037129}, {'dimension': [30, 10], 'name': 'object_5', 'position': (486, -1151), 'point': 5, 'angle': 0.3217505543966423}, {'dimension': [-9, 74], 'name': 'object_6', 'position': (183, -675), 'point': 5, 'angle': 1.6918235466041016}, {'dimension': [-38, -41], 'name': 'object_7', 'position': (1029, -631), 'point': 5, 'angle': 2.3182380450040307}, {'dimension': [7, 6], 'name': 'object_8', 'position': (457, -95), 'point': 10, 'angle': 0.7086262721276703}, {'dimension': [-42, -37], 'name': 'object_9', 'position': (955, -234), 'point': 10, 'angle': 2.419401322089805}, {'dimension': [-81, 57], 'name': 'object_10', 'position': (1411, -954), 'point': 10, 'angle': 2.5283853047152838}, {'dimension': [-27, -16], 'name': 'object_11', 'position': (1288, -801), 'point': 10, 'angle': 2.6066375798036967}, {'dimension': [-36, 47], 'name': 'object_12', 'position': (509, 207), 'point': 15, 'angle': 2.2244322237144183}, {'dimension': [-15, -10], 'name': 'object_13', 'position': (62, 140), 'point': 15, 'angle': 2.5535900500422257}, {'dimension': [53, 21], 'name': 'object_14', 'position': (1147, 178), 'point': 15, 'angle': 0.37724905964235905}, {'dimension': [31, -86], 'name': 'object_15', 'position': (1291, -253), 'point': 20, 'angle': 1.2248290541821005}, {'dimension': [70, 66], 'name': 'object_16', 'position': (1127, -370), 'point': 20, 'angle': 0.7559948751934432}, {'dimension': [-35, -80], 'name': 'object_17', 'position': (947, -755), 'point': 25, 'angle': 1.9832067683922838}, {'dimension': [7, 33], 'name': 'object_18', 'position': (1133, -956), 'point': 25, 'angle': 1.361773383988632}, {'dimension': [-33, 83], 'name': 'object_19', 'position': (1234, -1114), 'point': 30, 'angle': 1.9492237048235737}, {'dimension': [78, -5], 'name': 'object_20', 'position': (1494, -367), 'point': 30, 'angle': 0.0640149778343446}, {'dimension': [74, -74], 'name': 'object_21', 'position': (89, 268), 'point': -20, 'angle': 0.7853981633974484}, {'dimension': [52, -32], 'name': 'object_22', 'position': (757, -10), 'angle': 0.5516549825285467}, {'dimension': [47, -43], 'name': 'object_23', 'position': (214, -865), 'angle': 0.7409829481505374}, {'dimension': [-37, -79], 'name': 'object_24', 'position': (451, -286), 'angle': 2.008808527274025}]}
    print(selectionTarget(2))
