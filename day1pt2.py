import math
def findNeededFuel(mass):
	requiredFuel = math.floor(int(mass)/3)-2
	print("Mass = " + str(mass) + "; fuel is " + str(requiredFuel))
	return requiredFuel

input = open("day1pt1input.txt")
totalFuel = 0
for mass in input:
	fuelThisModule = findNeededFuel(mass.strip())
	newExtraMass = fuelThisModule
	while newExtraMass > 0:
		extraFuel = findNeededFuel(newExtraMass)
		print("Adding " + str(extraFuel) + " to account for " + str(newExtraMass) + " added for previous fuel")
		if extraFuel > 0:
			fuelThisModule += extraFuel
		newExtraMass = extraFuel
		print("New total = " + str(fuelThisModule))
	print("Final fuel amount found: " + str(fuelThisModule))
	totalFuel += fuelThisModule
	print(totalFuel)
print(totalFuel)
