def operateSet(first, second, third, fourth, fullInput):
	result = 0
	if(first == 1):
		result = inputArray[second] + inputArray[third]
	elif(first == 2):
		result = inputArray[second] * inputArray[third]
	if(first == 1 or first == 2):
		# assign value to the fourth position
		fullInput[fourth] = result
		print(str(first) + " first value, operation on " + str(second) + " and " + str(third) + " set to position " + str(fourth) + " (result value is " + str(result) + ")")
	else:
		print("first value was 99, terminating process")
	return fullInput
	
input = open("day2input.txt")
inputArray = []
for line in input:
	for item in line.split(","):
		inputArray.append(int(item))
print(inputArray)
startPosition = 0
while(startPosition+3 < len(inputArray) and inputArray[startPosition] != 99):
	inputArray = operateSet(inputArray[startPosition], inputArray[startPosition+1], inputArray[startPosition+2], inputArray[startPosition+3], inputArray)
	startPosition += 4
	print(inputArray)
if(startPosition < len(inputArray) and inputArray[startPosition] == 99):
	print("Opcode 99 detected, terminating")
print(inputArray)