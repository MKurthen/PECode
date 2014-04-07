#4.7s
from time import time
from PrimeNumbers import PrimeNumbers #self coded, works only if PrimeNumbers.py is in PYTHONPATH

StartTime = time()
limit = 1000000

PrimeNumbers = PrimeNumbers(limit)

Sieve = list()
# beginning with 2:
for i in range(limit):
	Sieve.append(set())

for i in PrimeNumbers:
	for j in range(1,(limit//i)+1):
		if ((j*i)-2) < limit:
			Sieve[(j*i)-2].add(i)

for i in range(3,len(Sieve)):
	if all(len(Sieve[j]) == 4 for j in range(i-3,i+1)):
		print(i)	
		break

print(time() - StartTime, 'seconds')
