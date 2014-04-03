#11.8s
from time import time
from math import floor, ceil, sqrt

StartTime = time()

Limit = 1000000
#############################
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
PrimeNumbers.add(5)
for n in range(5,Limit):
	if PrimeNumber[n-1] and (('2' not in str(n)) and ('4' not in str(n)) and ('5' not in str(n)) and ('6' not in str(n)) and ('8' not in str(n)) and ('0' not in str(n)) ): #Prime Numbers containing 2,4,5,6,8 or 0 can't be circular Primes (except 2,3,5) 
		PrimeNumbers.add(n)

###############################
count = 0
for i in PrimeNumbers:
	Str = str(i)
	CircPrime = True
	for k in range(len(Str)-1):
		Str = Str[1:]+Str[0]
		if int(Str) not in PrimeNumbers:
			CircPrime = False
			break
	if CircPrime:
		count += 1
	


print(time()-StartTime)
