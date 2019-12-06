import math

def doNextStep(listOfWires, step):
	stepDirection = step[0]
	stepAmount = int(step[1:])
	for x in range(int(stepAmount)):
		if len(listOfWires) > 0:
			lastWirePosition = listOfWires[len(listOfWires)-1]
		else:
			lastWirePosition = "0, 0"
		if(stepDirection == "U"):
			listOfWires.append(str(int(lastWirePosition.split(",")[0].strip())) + ", " + str(int(lastWirePosition.split(",")[1].strip())+1))
		elif(stepDirection == "D"):
			listOfWires.append(str(int(lastWirePosition.split(",")[0].strip())) + ", " + str(int(lastWirePosition.split(",")[1].strip())-1))
		elif(stepDirection == "R"):
			listOfWires.append(str(int(lastWirePosition.split(",")[0].strip())+1) + ", " + str(int(lastWirePosition.split(",")[1].strip())))
		elif(stepDirection == "L"):
			listOfWires.append(str(int(lastWirePosition.split(",")[0].strip())-1) + ", " + str(int(lastWirePosition.split(",")[1].strip())))
	return listOfWires

inputLine = open("day3Input.txt")
allWires = []
crosses = []
lengths = []
stepsToGetThere = []
lengths.append(99999999999999999999999999999999999999999999999999999999999999999999999)
stepsTaken = 0
for inputSet in inputLine:
	allWires.append([])
	for inputs in inputSet.split(","):
		allWires[len(allWires)-1] = doNextStep(allWires[len(allWires)-1], inputs)
for mainPoint in allWires[0]:
	stepsTaken = stepsTaken+1
	#print(mainPoint)
	length = abs(int(mainPoint.split(",")[0].strip()) + int(mainPoint.split(",")[1].strip()))
	match = True
	stepsOtherWires = 0
	for otherWire in allWires[1:]:
		if mainPoint not in otherWire:
			match = False
		else:
			#add the position of that value in otherwire to the stepsOtherWires value
			stepsOtherWires += otherWire.index(mainPoint) + 1
	if match:
		print("found match!!!")
		crosses.append(mainPoint)
		lengths.append(length)
		stepsToGetThere.append(stepsTaken + stepsOtherWires)
		print("First wire is on step " + str(stepsTaken) + " and the second wire is on step " + str(stepsOtherWires))
print(crosses)
print(lengths)
print(stepsToGetThere)
print("The smallest combined length is " + str(min(stepsToGetThere)))