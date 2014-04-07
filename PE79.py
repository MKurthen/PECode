#0.002s, HOWEVER if one digit would occur twice in the combination, this approach would NOT work
#Explanation: for each 3-digit attempt, create a tuple of each 2 digits((1st,2nd),(1st,3rd),(2nd,3rd)) in the order they appear
#	then, for each digit that appears in the login-attempts, look up which digits appear before (and after),
#		by this way determine where to insert each digit in the combination

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
	Digit1 = Attempt[1]
	Digit2 = Attempt[2]
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
#			if ComparisonOrder[0] == Digit:
#				DigitsAfterDigit.add(ComparisonOrder[1])
			if ComparisonOrder[1] == Digit:
				DigitsBeforeDigit.add(ComparisonOrder[0])
		InsertIndex = 0
		for ComparisonDigit in DigitsBeforeDigit:
			if ComparisonDigit in Combination:
				InsertIndex = max(InsertIndex, Combination.index(ComparisonDigit)+1)
		Combination.insert((InsertIndex),Digit)

print('Combination is ', ''.join(str(i) for i in Combination))
print(time()-StartTime, 'seconds')
