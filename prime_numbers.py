from math import floor,ceil, sqrt
import time
starttime = time.time()

limit = 10000000# upper limit for numbers to be searched for primes

"""
#Eratosthenes Sieve - finds all prime numbers up to a limit, returns them as list 'primes'
#8.5s for limit = 100k
primes = [2, 3]
PrimeNumber = [True] * ((limit//2)-1)
while True in PrimeNumber:
  x = PrimeNumber.index(True)
  y = x*2 + 5
  primes.append(y)
  for i in range((x), len(PrimeNumber), y):
    PrimeNumber[i] = False
"""

#Atkins Sieve
#0.3s for limit = 100k, 2.8s for limit = 1M
PrimeNumber = (limit)*[False]
for x in range(1,ceil(sqrt(limit))):
	for y in range(1,ceil(sqrt(limit))):
		n = (4*(x**2)) + (y**2)
		if (n <=limit) and ((n % 12 == 1) or (n % 12 == 5)):
			PrimeNumber[n-1] = not PrimeNumber[n-1]
		n = (3*(x**2)) + (y**2)
		if (n <= limit) and (n % 12 == 7):
			PrimeNumber[n-1] = not PrimeNumber[n-1]
		n = (3*(x**2)) - (y**2)
		if (x > y) and (n <= limit) and (n % 12 == 11):
			PrimeNumber[n-1] = not PrimeNumber[n-1]	

for n in range(5, ceil(sqrt(limit))):
	if PrimeNumber[n-1]:
		for k in range((n**2),limit,(n**2)):
			PrimeNumber[k-1] = False

PrimeNumbers = [2,3]
for n in range(5,limit):
	if PrimeNumber[n-1]:
		PrimeNumbers.append(n)


print (time.time() -starttime), "seconds"
