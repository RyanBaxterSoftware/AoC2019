import math
def findNeededFuel(mass):
	requiredFuel = math.floor(int(mass.strip())/3)-2
	print("Mass = " + mass.strip() + "; fuel is " + str(requiredFuel))
	return requiredFuel

input = open("day1pt1input.txt")
totalFuel = 0
for mass in input:
	totalFuel += findNeededFuel(mass)
	print(totalFuel)
print(totalFuel)