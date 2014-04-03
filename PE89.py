from copy import deepcopy

txt = open('/home/Max/code/PECode/PE89Roman.txt').readlines()
InputNumbers = list()
for i in range(len(txt)):
	print(i)
	InputNumbers.append(txt[i].replace('\n', ''))

def ReplaceWithHigherDigitsRule(InputNumber): #changes one occurence of unnecassary digits, returns New Number, returns Input if no such occurence found
	for i in range(len(InputNumber)):
		if i >= 1 and (InputNumber[i] == InputNumber[i-1]):
			#two V's to one X
			if InputNumber[i] == 'V':
				OutputNumber = InputNumber[:(i-1)] + 'X' + InputNumber[(i+1):]
				break
			#two L's to one C
			if InputNumber[i] == 'L':
				OutputNumber = InputNumber[:(i-1)] + 'C' + InputNumber[(i+1):]
				break
			#two D's to one M
			if InputNumber[i] == 'D':
				OutputNumber = InputNumber[:(i-1)] + 'M' + InputNumber[(i+1):]
				break
		if i >= 4 and (InputNumber[i] == InputNumber[i-1] == InputNumber[i-2] == InputNumber[i-3] == InputNumber[i-4]):
			#five I's to one V
			if InputNumber[i] == 'I':
				OutputNumber = InputNumber[:(i-4)] + 'V' + InputNumber[(i+1):]
				break
			#five X's to one L
			if InputNumber[i] == 'X':
				OutputNumber = InputNumber[:(i-4)] + 'L' + InputNumber[(i+1):]
				break
			# five C's to one D 
			if InputNumber[i] == 'C':
				OutputNumber = InputNumber[:(i-4)] + 'D' + InputNumber[(i+1):]
				break
		if i == len(InputNumber)-1:	
			OutputNumber = InputNumber
			break
	return OutputNumber

def ReplaceSubstractiveRule(InputNumber):
	for i in range(len(InputNumber)):
		if i >= 3 and (InputNumber[i] == InputNumber[i-1] == InputNumber[i-2] == InputNumber[i-3]):
			#four I's to one IV
			if InputNumber[i] == 'I':
				OutputNumber = InputNumber[:(i-3)] + 'IV' + InputNumber[(i+1):]
				break
			#four X's to one XL
			if InputNumber[i] == 'X':
				OutputNumber = InputNumber[:(i-3)] + 'XL' + InputNumber[(i+1):]
				break
			#four C's to one CD
			if InputNumber[i] == 'C':
				OutputNumber = InputNumber[:(i-3)] + 'CD' + InputNumber[(i+1):]
				break
		if i == len(InputNumber)-1:	
			OutputNumber = InputNumber
	return OutputNumber

def CorrectWrongSubstractions(InputNumber):
	for i in range(len(InputNumber)):
		#replace VIV with IX
		if i >= 2 and ((InputNumber[i] == 'V') and (InputNumber[i-1] == 'I') and ( InputNumber[i-2] == 'V')):
			OutputNumber = InputNumber[:(i-2)] + 'IX' + InputNumber[(i+1):]
			break
		#replace LXL with XC 
		if i >= 2 and ((InputNumber[i] == 'L') and (InputNumber[i-1] == 'X') and ( InputNumber[i-2] == 'L')):
			OutputNumber = InputNumber[:(i-2)] + 'XC' + InputNumber[(i+1):]
			break
		#replace DCD with CM
		if i >= 2 and ((InputNumber[i] == 'D') and (InputNumber[i-1] == 'C') and ( InputNumber[i-2] == 'D')):
			OutputNumber = InputNumber[:(i-2)] + 'CM' + InputNumber[(i+1):]
			break
		if i == len(InputNumber)-1:	
			OutputNumber = InputNumber
	return OutputNumber

NumberOfCharactersBefore = 0
for number in InputNumbers:
	NumberOfCharactersBefore += len(number)

#step 1:
InputNumbersCopy = deepcopy(InputNumbers)
CorrectedNumbersStage1 = list()
while len(InputNumbers) > 0:
	if len(InputNumbers[0]) == 0:
		InputNumbers.pop(0)
	OutputNumber = ReplaceWithHigherDigitsRule(InputNumbers[0])
	if OutputNumber == InputNumbers[0]: 
		InputNumbers.pop(0)
		CorrectedNumbersStage1.append(OutputNumber)
	else: 
		InputNumbers[0] = OutputNumber
	counter += 1

#step2
CorrectedNumbersStage2 = list()
while len(CorrectedNumbersStage1) > 0:
	OutputNumber = ReplaceSubstractiveRule(CorrectedNumbersStage1[0])
	if OutputNumber == CorrectedNumbersStage1[0]:
		CorrectedNumbersStage2.append(OutputNumber)
		CorrectedNumbersStage1.pop(0)
	else: 
		CorrectedNumbersStage1[0] = OutputNumber

#step3
CorrectedNumbersStage3 = list()
while len(CorrectedNumbersStage2) > 0:
	OutputNumber = CorrectWrongSubstractions(CorrectedNumbersStage2[0])
	if OutputNumber == CorrectedNumbersStage2[0]:
		CorrectedNumbersStage3.append(OutputNumber)
		CorrectedNumbersStage2.pop(0)
	else: 
		CorrectedNumbersStage2[0] = OutputNumber

NumberOfCharactersAfter=0
for number in CorrectedNumbersStage3:
	NumberOfCharactersAfter += len(number)

print((NumberOfCharactersBefore - NumberOfCharactersAfter), 'characters less')

	
