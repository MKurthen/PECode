#First create a List with all Prime numbers which could be needed, then check systematically through all possible combinations of a and b where n**2 + an + b produces the longest chain of prime for n starting with 0, raised by 1
#5.27s after changing PrimeNumbers from list to set ( accelerated lookup)
from time import time
from math import floor, ceil, sqrt

StartTime = time()

AbsLimita = 1000
AbsLimitb = 1000 
Limit = 1000000

#Atkins Sieve
PrimeNumber = (Limit)*[False]
for x in range(1,ceil(sqrt(Limit))):
	for y in range(1,ceil(sqrt(Limit))):
		n = (4*(x**2)) + (y**2)
		if (n <=Limit) and ((n % 12 == 1) or (n % 12 == 5)):
			PrimeNumber[n-1] = not PrimeNumber[n-1]
		n = (3*(x**2)) + (y**2)
		if (n <= Limit) and (n % 12 == 7):
			PrimeNumber[n-1] = not PrimeNumber[n-1]
		n = (3*(x**2)) - (y**2)
		if (x > y) and (n <= Limit) and (n % 12 == 11):
			PrimeNumber[n-1] = not PrimeNumber[n-1]	
for n in range(5, ceil(sqrt(Limit))):
	if PrimeNumber[n-1]:
		for k in range((n**2),Limit,(n**2)):
			PrimeNumber[k-1] = False
PrimeNumbers = set()
PrimeNumbers.add(2)
PrimeNumbers.add(3)
for n in range(5,Limit):
	if PrimeNumber[n-1]:
		PrimeNumbers.add(n)

Results = [0,0,0] # store results for a, b and max chainlength
for a in range(-AbsLimita,AbsLimita):
	print(a) #Progress
	for b in range(-AbsLimitb,AbsLimitb):
		n = 0
		counter = 0
		while ((n**2 )+ (a*n) +(b) in PrimeNumbers):
				counter += 1
				n += 1
#		for n in range(100000): #no limit for n is given in the question, however an endless loop should be avoided
			#if (n**2 + a*n + b) in PrimeNumbers:
			#	counter +=1
			#else: 
		#		if (n**2+a*n+b) > Limit:
		#			print((n**2+a*n+b), 'over Limit') # Alert, too less Prime Numbers calculated
		#		break
		#overwrite result list, if counter reaches new maximum
		if counter > Results[2]:
			Results = [a,b,counter]




print(time()-StartTime)
