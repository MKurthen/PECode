import time
from math import sqrt, ceil
StartTime = time.time()


limit = 1000000

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

#square numbers until 1M
Squares = list()
for i in range(1,int(ceil(limit))):
	Squares.append(i**2)

for i in range(1,int(limit/2)):
	if j %100 == 0:
		print(j)
	j = 2*i +1
	if j in PrimeNumbers:
		continue
	candidate = True
	for k in Squares:
		if (j - 2*k) in PrimeNumbers:
			candidate = False
			break
		if (j-2*k) < 0:
			break
	if candidate:
		print(j)
		break

print (time.time() -StartTime), "seconds"

