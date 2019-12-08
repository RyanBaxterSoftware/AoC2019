import msvcrt

def operateSet(opcode, fullInput):
	global currentInput
	terminate = False
	opcode = str(opcode) # opcode is converted to string for easier adjustment
	while len(opcode) < 2:
		opcode = "0" + opcode
	result = 0
	numInputs = 0
	typeOfOperation = opcode
	while len(typeOfOperation) > 2: # we only want the last two values
		typeOfOperation = typeOfOperation[1:]
	if(typeOfOperation == "01"):
		while len(opcode) < 5:
			opcode = "0" + opcode
		print(str(opcode))
		firstValue = fullInput[fullInput[currentInput+1]] if opcode[2] == '0' else fullInput[currentInput+1]
		secondValue = fullInput[fullInput[currentInput+2]] if opcode[1] == '0' else fullInput[currentInput+2]
		result = int(firstValue) + int(secondValue)
		fullInput[fullInput[currentInput+3]] = result
		print(str(firstValue) + " and " + str(secondValue) + " being added together: " + str(result) + " and saved to " + str(currentInput+3))
		currentInput += 4
	elif(typeOfOperation == "02"):
		while len(opcode) < 5:
			opcode = "0" + opcode
		print(str(opcode))
		firstValue = fullInput[fullInput[currentInput+1]] if opcode[2] == '0' else fullInput[currentInput+1]
		secondValue = fullInput[fullInput[currentInput+2]] if opcode[1] == '0' else fullInput[currentInput+2]
		result = firstValue * secondValue
		fullInput[fullInput[currentInput+3]] = result
		print(str(firstValue) + " and " + str(secondValue) + " being multiplied together: " + str(result) + " and saved to " + str(currentInput+3))
		currentInput += 4
	elif typeOfOperation == "03":
		print("Enter the value to be saved")
		fullInput[fullInput[currentInput+1]] = int(input())
		currentInput += 2
	elif typeOfOperation == "04":
		while len(opcode) < 3:
			opcode = "0" + opcode
		print(str(fullInput[fullInput[currentInput+1]] if opcode[0] == '0' else fullInput[currentInput+1]))
		print("That was a printed value from opcode " + opcode + " with input " + str(fullInput[fullInput[currentInput+1]] if opcode[0] == '0' else fullInput[currentInput+1]))
		currentInput += 2
	elif(typeOfOperation == "05"): # all these added values need to be adjusted to accept literals
		while len(opcode) < 4:
			opcode = "0" + opcode
		print(str(opcode))
		testedValue = (fullInput[fullInput[currentInput+1]] if opcode[1] == '0' else fullInput[currentInput+1])
		setValue = (fullInput[fullInput[currentInput+2]] if opcode[0] == '0' else fullInput[currentInput+2])
		if testedValue is not 0:
			currentInput = setValue
			print(str(testedValue) + " is not 0 so the next step will be " + str(setValue))
		else:
			print(str(testedValue) + " is 0 so the next step will be " + str(currentInput+3))
			currentInput += 3
	elif(typeOfOperation == "06"):
		while len(opcode) < 4:
			opcode = "0" + opcode
		print(str(opcode))
		testedValue = (fullInput[fullInput[currentInput+1]] if opcode[1] == '0' else fullInput[currentInput+1])
		setValue = (fullInput[fullInput[currentInput+2]] if opcode[0] == '0' else fullInput[currentInput+2])
		if testedValue is 0:
			print(str(testedValue) + " is 0 so the next step will be " + str(setValue))
			currentInput = setValue
		else:
			print(str(testedValue) + " is not 0 so the next step will be " + str(currentInput+3))
			currentInput += 3
	elif(typeOfOperation == "07"):
		while len(opcode) < 5:
			opcode = "0" + opcode
		print(opcode)
		firstNum = fullInput[fullInput[currentInput+1]] if opcode[2] == '0' else fullInput[currentInput+1]
		secondNum = fullInput[fullInput[currentInput+2]] if opcode[1] == '0' else fullInput[currentInput+2]
		answer = 0
		if firstNum < secondNum:
			answer = 1
			print(str(firstNum) + " is less than " + str(secondNum) + " so 1 is being saved to " + str(fullInput[currentInput+3]))
		else:
			print(str(firstNum) + " is not less than " + str(secondNum) + " so 0 is being saved to " + str(fullInput[currentInput+3]))
		fullInput[fullInput[currentInput+3]] = answer
		currentInput += 4
	elif(typeOfOperation == "08"):
		while len(opcode) < 5:
			opcode = "0" + opcode
		print(str(opcode))
		firstNum = fullInput[fullInput[currentInput+1]] if opcode[2] == '0' else fullInput[currentInput+1]
		secondNum = fullInput[fullInput[currentInput+2]] if opcode[1] == '0' else fullInput[currentInput+2]
		answer = 0
		if firstNum == secondNum:
			answer = 1
			print(str(firstNum) + " is equal to " + str(secondNum) + " so 1 is being saved to " + str(fullInput[currentInput+3]))
		else:
			print(str(firstNum) + " is not equal to " + str(secondNum) + " so 0 is being saved to " + str(fullInput[currentInput+3]))
		print("Answer is " + str(answer) + " and position is " + str(currentInput+3))
		fullInput[fullInput[currentInput+3]] = answer
		print("This one? " + str(fullInput))
		currentInput += 4
	elif(typeOfOperation == "99"):
		terminate = True # impossible result marks that the program should be stopped
	else:
		print("out of bounds error")
		terminate = True
	return (fullInput, terminate)
	
inputFile = open("day5Input.txt")
inputArray = []
for line in inputFile:
	for item in line.split(","):
		inputArray.append(int(item))
#print("original is " + str(inputArray))
currentInput = 0
terminateNow = False
while(currentInput < len(inputArray) and not terminateNow):
	answers = operateSet(inputArray[currentInput], inputArray)
	inputArray = answers[0]
	terminateNow = answers[1]
	print(str(inputArray))
if(terminateNow):
	print("terminating")