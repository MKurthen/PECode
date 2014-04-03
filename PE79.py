from time import time

StartTime = time()

Attempts = list()
txt = open('/home/Max/code/PECode/PE79Keylog.txt').readlines()
for line in txt:
	CleanLine = line.replace('\n','')
	Attempt = list(CleanLine)
	for i in range(len(Attempt)):
		Attempt[i] = int(Attempt[i])
	Attempts.append(Attempt)

Combination = Attempts[0]
Orders = []
for Attempt in Attempts:
	Digit0 = Attempt[0]
	FirstDigitIn = [[],[]]
	for i in range(len(Attempts)):
		CompAttempt = Attempts[i]
		for j in range(len(CompAttempt)):
			if CompAttempt[j] == Digit0:
				FirstDigitIn[0].append(i)
				FirstDigitIn[1].append(j)
	Digit1 = Attempt[1]
	SecondDigitIn = list()
	for i in range(len(Attempts)):
		CompAttempt = Attempts[i]
		for j in range(len(CompAttempt)):
			if CompAttempt[j] == Digit1:
				SecondDigitIn.append([i,j])
	Digit2 = Attempt[2]
	ThirdDigitIn = list()
	for i in range(len(Attempts)):
		CompAttempt = Attempts[i]
		for j in range(len(CompAttempt)):
			if CompAttempt[j] == Digit2:
				ThirdDigitIn.append([i,j])
	if ([Digit0,Digit1] not in Orders):
		Orders.append([Digit0,Digit1])
	if ([Digit0,Digit2] not in Orders):
		Orders.append([Digit0,Digit2])
	if ([Digit1,Digit2] not in Orders):
		Orders.append([Digit1,Digit2])
	
for Order in Orders:
	if ([Order[1],Order[0]] in Orders):
		print('Error',Order[0],Order[1])
Combination = []
Flag = False
while not Flag:
	Flag = True
	for Order in Orders:
		if (Order[0] in Combination) and (Order[1] in Combination):
			continue
		if (Order[0] not in Combination):
			Digit = Order[0]
			Flag = False
		elif (Order[1] not in Combination): 
			Digit = Order[1]
			Flag = False
		DigitsBeforeDigit =  set()
		DigitsAfterDigit = set()
		for ComparisonOrder in Orders:
			if ComparisonOrder[0] == Digit:
				DigitsAfterDigit.add(ComparisonOrder[1])
			if ComparisonOrder[1] == Digit:
				DigitsBeforeDigit.add(ComparisonOrder[0])
		InsertIndex = 0
		for Digit in DigitsBeforeDigit:
			if Digit in Combination:
				InsertIndex = max(InsertIndex, Combination.index(Digit))
		Combination.insert((InsertIndex+1),Digit)
		print(Combination)
"""
#for every digit in TryCombination:
#	if 2 digits found in reverseOrder in another attempt:
#		

TryCombination = Attempts[0]
	Digit0 = TryCombination[0]
	FirstDigitIn = [[],[]]
	for i in range(len(Attempts)):
		CompAttempt = Attempts[i]
		for j in range(len(CompAttempt)):
			if CompAttempt[j] == Digit0:
				FirstDigitIn[0].append(i)
				FirstDigitIn[1].append(j)
	Digit1 = TryCombination[1]
	SecondDigitIn = list()
	for i in range(len(Attempts)):
		CompAttempt = Attempts[i]
		for j in range(len(CompAttempt)):
			if CompAttempt[j] == Digit1:
				SecondDigitIn.append([i,j])
	Digit2 = Attempt[2]
	ThirdDigitIn = list()
	for i in range(len(Attempts)):
		CompAttempt = Attempts[i]
		for j in range(len(CompAttempt)):
			if CompAttempt[j] == Digit2:
Combination = Attempts[0]
for Attempt in Attempts:
				ThirdDigitIn.append([i,j])
"""
