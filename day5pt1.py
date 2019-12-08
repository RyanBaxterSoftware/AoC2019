import msvcrt

currentInput = 0 # global value to hold the current input value

def operateSet(opcode, fullInput):
	opcode = str(opcode) # opcode is converted to string for easier adjustment
	while len(opcode) < 2:
		opcode = "0" + opcode
	result = 0
	numInputs = 0
	typeOfOperation = opcode
	while len(typeOfOperation) > 2: # we only want the last two values
		typeOfOperation = typeOfOperation[1:]
	if(typeOfOperation == "01"):
		numInputs = 4
		while len(opcode) < 5:
			opcode = "0" + opcode
		#print(str(opcode))
		firstValue = fullInput[fullInput[currentInput+1]] if opcode[2] == '0' else fullInput[currentInput+1]
		secondValue = fullInput[fullInput[currentInput+2]] if opcode[1] == '0' else fullInput[currentInput+2]
		result = int(firstValue) + int(secondValue)
		fullInput[fullInput[currentInput+3]] = result
		#print(str(firstValue) + " and " + str(secondValue) + " being added together: " + str(result) + " and saved to " + str(currentInput+3))
	elif(typeOfOperation == "02"):
		numInputs = 4
		while len(opcode) < 5:
			opcode = "0" + opcode
		#print(str(opcode))
		firstValue = fullInput[fullInput[currentInput+1]] if opcode[2] == '0' else fullInput[currentInput+1]
		secondValue = fullInput[fullInput[currentInput+2]] if opcode[1] == '0' else fullInput[currentInput+2]
		result = firstValue * secondValue
		fullInput[fullInput[currentInput+3]] = result
		#print(str(firstValue) + " and " + str(secondValue) + " being multiplied together: " + str(result) + " and saved to " + str(currentInput+3))
	elif typeOfOperation == "03":
		numInputs = 2
		print("Enter the value to be saved")
		fullInput[fullInput[currentInput+1]] = input()
	elif typeOfOperation == "04":
		numInputs = 2
		while len(opcode) < 3:
			opcode = "0" + opcode
		print(str(fullInput[fullInput[currentInput+1]] if opcode[0] == '0' else fullInput[currentInput+1]))
	elif(typeOfOperation == "99"):
		numInputs = -1 # impossible result marks that the program should be stopped
	else:
		print("out of bounds error")
	return (fullInput, numInputs)
	
inputFile = open("day5input.txt")
inputArray = []
for line in inputFile:
	for item in line.split(","):
		inputArray.append(int(item))
print("original is " + str(inputArray))
currentInput = 0
terminateNow = 0
while(currentInput < len(inputArray) and not terminateNow):
	answers = operateSet(inputArray[currentInput], inputArray)
	inputArray = answers[0]
	terminateNow = answers[1] == -1
	currentInput += answers[1]
if(terminateNow):
	print("Opcode 99 detected, terminating")