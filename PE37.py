#10.5s

from math import sqrt, ceil, floor
from time import time
from copy import deepcopy

StartTime = time()
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

ResultNumbers = set()
for i in PrimeNumbers:
	j = str(i)
	while int(j) in PrimeNumbers:
		if len(j) == 1:
			k = str(i)
			while int(k) in PrimeNumbers:
				if len(k) == 1:
					ResultNumbers.add(i)
					break
				k = k[1:]
			break
		j = j[:-1]


ResultNumbers.remove(2)
ResultNumbers.remove(3)
ResultNumbers.remove(5)
ResultNumbers.remove(7)
	 
print((time() - StartTime), 'seconds')

