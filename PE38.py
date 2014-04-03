#0.05s
from time import time
StartTime = time()

Limit = 9999

ResultNumbers = set()
LargestPandigital = 0
for i in range(Limit):
	if i % 10 == 0:
		print(i)
	pandigital = False
	k = 1
	ConcProd = ''
	while len(ConcProd) < 9:
		ConcProd = ConcProd + str(k*i)
		if len(ConcProd) > 9:
			pandigital = False
		if len(ConcProd) == 9:
			for j in range(1,10):
				if str(j) not in ConcProd:
					break
			else:
				pandigital = True
				ResultNumbers.add(i)
				LargestPandigital = max([LargestPandigital, int(ConcProd)]) 
		k += 1

print((time()-StartTime), 'seconds')


