debug = False

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

def getDistanceBetweenPoints(points, point1, point2):
	totalDistance = 0
	pointsWithChildren = [] # to be used if both points don't have a contianed point
	for point in points:
		if point.hasChildOrbital(point1) and point.hasChildOrbital(point2):
			thereWasAParentPoint = True
			thisPoint = point
			aDeeperPoint = True
			while aDeeperPoint:
				aDeeperPoint = False
				for child in thisPoint.childOrbitals:
					if child.hasChildOrbital(point1) and child.hasChildOrbital(point2):
						aDeeperPoint = True
						thisPoint = child
			print("The deepest point is " + thisPoint.name)
			# this will be the deepest point that is a parent to both points
			totalDistance += thisPoint.getDepthOfChild(point1)
			totalDistance += thisPoint.getDepthOfChild(point2)
		elif point.hasChildOrbital(point1) or point.hasChildOrbital(point2):
			pointsWithChildren.add(point)
	if len(pointsWithChildren) >= 2:
		for point in pointsWithChildren:
			totalDistance += point.getDepthOfChild(point1)
			totalDistance += point.getDepthOfChild(point2) # this value is 0 if there is no child present
	return totalDistance
	# Find the deepest point that is a parent of both objects, then get the depth of both points (the solution will be off by one, not sure which way)
	# If there isn't a parent of both, we need to treat "nothing" as a point too

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
		global debug
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
		
	def getDepthOfChild(self, child):
		depth = 0
		thisPoint = self
		print("About to calculate depth")
		pathDown = []
		while thisPoint.name != child and thisPoint.hasChildOrbital(child):
			pathDown.append(thisPoint.name)
			for point in thisPoint.childOrbitals:
				if point.hasChildOrbital(child) or point.name == child:
					thisPoint = point
					depth += 1
		print("Calculating depth: " + str(depth))
		print(str(pathDown))
		print(str(len(pathDown)))
		return depth - 1 # because we don't count the base depth or the final point, and the final point already isn't being counted
		#keep track of how deep you have to go to find the requested point

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
debug = True
print(str(getDistanceBetweenPoints(pointsContainingWanted, "SAN", "YOU")))