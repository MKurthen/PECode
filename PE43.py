from time import time
from math import floor, ceil

StartTime = time()

def recurse(m):
	if m == 9:
		return m
	else:
		recurse(m+1)
	print(m)
	return m

def RecurseBlock(m):
	True

for m in [2,3,5,7,11,13,17]:
	for i in range(ceil(100.0/m),floor(999.0/m)+1):
		block = str(i*m)
