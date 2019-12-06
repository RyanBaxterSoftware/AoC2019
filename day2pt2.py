import msvcrt

def operateSet(first, second, third, fourth, fullInput):
	result = 0
	if(first == 1):
		result = fullInput[second] + fullInput[third]
	elif(first == 2):
		result = fullInput[second] * fullInput[third]
	if(first == 1 or first == 2):
		# assign value to the fourth position
		if(fourth < len(fullInput)):
			fullInput[fourth] = result
		else:
			print("out of bounds error")
	return fullInput
	
input = open("day2input.txt")
inputArray = []
for line in input:
	for item in line.split(","):
		inputArray.append(int(item))
solution = "no"
for x in range(0, 100):
	for y in range(0, 100):
		print("original is " + str(inputArray))
		inputArrayThisTime = []
		for pos in range(len(inputArray)):
			inputArrayThisTime.append(inputArray[pos])
		inputArrayThisTime[1] = x
		inputArrayThisTime[2] = y
		print(inputArrayThisTime);
		startPosition = 0
		while(startPosition+3 < len(inputArrayThisTime) and inputArrayThisTime[startPosition] != 99):
			inputArrayThisTime = operateSet(inputArrayThisTime[startPosition], inputArrayThisTime[startPosition+1], inputArrayThisTime[startPosition+2], inputArrayThisTime[startPosition+3], inputArrayThisTime)
			startPosition += 4
		if(startPosition < len(inputArrayThisTime) and inputArrayThisTime[startPosition] == 99):
			print("Opcode 99 detected, terminating")
		print(inputArrayThisTime[0])
		if(inputArrayThisTime[0] == 19690720):
			print("HEY IT'S THE THING!!! " + str(x) + " and " + str(y) + " give you 19690720")
			solution = str(x) + ", " + str(y)
print(solution + " in case you didn't catch it ;3")