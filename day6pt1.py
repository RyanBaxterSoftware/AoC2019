def getPoint(points, name):
	foundPoint = "point not found"
	numberFound = 0
	for point in points:
		if point.name == name:
			foundPoint = point
			numberFound += 1
		elif point.hasChildOrbital(name):
			foundPoint = getPoint(point.childOrbitals, name)
			numberFound += 1
	if numberFound > 1:
		print("HEY SOMETHING WENT WRONG MULTIPLES DETECTED")
		input()
	return foundPoint

def removePoint(points, soughtPoint):
	for point in points:
		if point.name == soughtPoint.name:
			points.remove(soughtPoint)
		if point.hasChildOrbital(soughtPoint.name):
			childIsImmediate = False
			thisPoint = point
			while not childIsImmediate:
				for child in thisPoint.childOrbitals:
					if child.name == point.name:
						childIsImmediate = True
						thisPoint.childOrbitals.remove(soughtPoint)
					elif child.hasChildOrbital(soughtPoint.name):
						thisPoint = child
				

class Point:
	
	def __init__(self, name):
		self.childOrbitals = []
		self.name = name
	
	def addOrbital(self, initialPoints, newOrbital):
		neededPoint = getPoint(initialPoints, newOrbital)
		if neededPoint != "point not found":
			removePoint(initialPoints, neededPoint)
			self.childOrbitals.append(neededPoint)
			
		else:
			self.childOrbitals.append(Point(newOrbital))
		
	def printPath(self, indent):
		line = indent * "    "
		line = line + "I am " + self.name + " and my children are "
		for child in self.childOrbitals:
			line = line + child.name + ", "
		print(line)
		for child in self.childOrbitals:
			child.printPath(indent+1)
		
	def hasChildOrbital(self, whichOrbital):
		childOrbitalFound = False
		childOrbitalsContainingChild = [] # this may be the orbital being looked for, as well
		for orbital in self.childOrbitals:
			if orbital.name == whichOrbital or orbital.hasChildOrbital(whichOrbital):
				childOrbitalFound = True
				childOrbitalsContainingChild.append(orbital)
			#if orbital.name == whichOrbital:
			#	print(orbital.name + " is the sought orbital")
			#elif orbital.hasChildOrbital(whichOrbital):
			#	print(orbital.name + " has a child orbital of " + whichOrbital)
			#else:
			#	print(orbital.name + " does not contain " + whichOrbital)
			#if orbital.name == "1Q7" and whichOrbital == "W3Q":
			#	input()
		return childOrbitalFound
		
	def getTotalLength(self, lengthSoFar):
		lengthFromThisPoint = lengthSoFar # for the fact that this is 1 more than the previous point
		for point in self.childOrbitals:
			lengthFromThisPoint += point.getTotalLength(lengthSoFar+1)
		return lengthFromThisPoint

inputFile = open("day6Input.txt")
initialPoints = []
instructions = []
for line in inputFile:
	orbital = line.split(")")
	instructions.append((orbital[0].strip(), orbital[1].strip()))
for instruction in instructions:
	print(str(instruction))
	pointsContainingWanted = []
	sourceExistsOrAdded = False
	for point in initialPoints:
		if point.name == instruction[0]:
			point.addOrbital(initialPoints, instruction[1])
			sourceExistsOrAdded = True
		if point.hasChildOrbital(instruction[0]):
			pointsContainingWanted.append(point)
			sourceExistsOrAdded = True
	for point in pointsContainingWanted:
		currentPoint = point
		while currentPoint.name != instruction[0]:
			for point in currentPoint.childOrbitals:
				if point.hasChildOrbital(instruction[0]) or point.name == instruction[0]:
					currentPoint = point
		currentPoint.addOrbital(initialPoints, instruction[1])
	if not sourceExistsOrAdded:
		initialPoints.append(Point(instruction[0]))
		initialPoints[len(initialPoints)-1].addOrbital(initialPoints, instruction[1])
print(str(instructions))
totalLength = 0
for point in initialPoints:
	point.printPath(0)
	totalLength += point.getTotalLength(0)
print(str(totalLength))