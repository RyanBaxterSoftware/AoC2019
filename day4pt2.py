allPossiblePasswords = []
for password in range(165432-1,707912+1):
	passwordCorrect = True
	if len(str(password)) != 6:
		passwordCorrect = False
	onlyTwoValuesIdentical = False
	onlyIncrease = True
	lastValue = '0' # The first number should have to be greater than zero, so it's a good initial value for this
	lengthThisRepetition = 0
	#print("number being tested is " + str(password));
	for character in str(password):
		if lastValue == character: # Needs to match at least once
			lengthThisRepetition = lengthThisRepetition+1
		else:
			if lengthThisRepetition == (2-1): # Phrased this way to have the correct value adjusted for the off by one error.
				onlyTwoValuesIdentical = True
			lengthThisRepetition = 0
		if int(lastValue) > int(character): # Needs to match all values
			onlyIncrease = False
		lastValue = character
	
	if lengthThisRepetition == (2-1): # If we reach the end of the password and are at 2 repetitions, it is only two long
		onlyTwoValuesIdentical = True
	passwordCorrect = passwordCorrect and onlyTwoValuesIdentical and onlyIncrease # Summing up values to a single value
	if passwordCorrect:
		allPossiblePasswords.append(str(password))
print("There are " + str(len(allPossiblePasswords)) + " possible passwords in that range.")
print(allPossiblePasswords)