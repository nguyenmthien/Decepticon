def moveToVertices(verticesAxisY):
	veticesArray= []
	
	
	for i in range(veticesAxisy):
		veticesArray.append(i)
	
	for count in range(len(veticesArray)):
		for count_1 in range(len(veticesArray) - count - 1):
			if (veticesArray[count + count_1 + 1] < veticesArray[count]):
				
				temporary = veticesArray[count]
				veticesArray[count] = veticesArray[count + count_1 + 1]
				veticesArray[count + count_1 + 1] = temporary
	
	verticesSelect = max(verticesArray);
	
if __name__=='__main__':
        verticesAxisY = [vertices['Manual Ally']['vertices1'][1]]
        moveToVertices(verticesAxisY)
