from math import floor,ceil, sqrt
import time
starttime = time.time()

limit = 100 # upper limit for numbers to be searched for primes

"""
#Eratosthenes Sieve - finds all prime numbers up to a limit, returns them as list 'primes'
#8.5s for limit = 100000
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
PrimeNumber = (limit-5)*[True]
for x in range(1,ceil(sqrt(limit))):
	for y in range(1,ceil(sqrt(limit))):
		n = (4*(x**2)) + (y**2)
		if (n <=limit) and ((n % 12 == 1) or (n % 12 == 5)):
			PrimeNumber[n] = not PrimeNumber[n]
		n = (3*(x**2)) + (y**2)
		if (n <= limit) and (n % 12 == 7):
			PrimeNumber[n] = not PrimeNumber[n]
		n = (3*(x**2)) - (y**2)
		if (x > y) and (n <= limit) and (n % 12 == 11)
			PrimeNumber[n] = not PrimeNumber[n]	
print (time.time() -starttime), "seconds"
