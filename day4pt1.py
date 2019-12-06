allPossiblePasswords = []
for password in range(165432-1,707912+1):
	passwordCorrect = True
	if len(str(password)) != 6:
		passwordCorrect = False
	twoValuesIdentical = False
	onlyIncrease = True
	lastValue = '0' # The first number should have to be greater than zero, so it's a good initial value for this
	#print("number being tested is " + str(password));
	for character in str(password):
		if lastValue == character: # Needs to match at least once
			twoValuesIdentical = True
		if int(lastValue) > int(character): # Needs to match all values
			onlyIncrease = False
		lastValue = character
	passwordCorrect = passwordCorrect and twoValuesIdentical and onlyIncrease # Summing up values to a single value
	if passwordCorrect:
		allPossiblePasswords.append(str(password))
print("There are " + str(len(allPossiblePasswords)) + " possible passwords in that range.")
print(allPossiblePasswords)