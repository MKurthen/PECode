#2.1s 
from time import time
from math import floor, ceil

StartTime = time()
M = [2,3,5,7,11,13,17]
numbers = []
Number = ''

def RecurseBlock(digit, n, numbers):
	for i in range(floor(999.0/M[digit])+1):
		block = str(i*M[digit])
		if len(block) == 1:
			block = '00' + block
		if len(block) == 2:
			block = '0' + block
		if not ((n[-2:] != block[:2]) or (block[2] in n)):
			n = n + block[2] 
			if digit == 6:
				numbers.append(n)
			else:
				RecurseBlock(digit+1, n, numbers)
			n = n[:-1]
d = 0
for k in range(0,10):
	
	Number += str(k)
	d = 0

	for i in range(floor(999.0/M[d])+int(1)):
		block = str(M[d]*i)
		if len(block) == 1:
			block = '00' + block
		if len(block) == 2:
			block = '0' + block
		if (Number in block) or any(block[j] in block[:j]+block[j+1:] for j in range(3)):
			continue
		else:
			Number += block 
			RecurseBlock(1, Number, numbers)
			Number = Number[:-3]
	
	Number = Number[:-1]

"""
#Expicit coded
def AppendZero(a):
	if len(str(a)) == 3:
		return str(a)
	if len(str(a)) == 2:
		return ('0' + str(a))
	if len(str(a)) == 1:
		return ('00' + str(a))

Number = ''
for a in range(10):
	Number += str(a)
	for b in range(1000):
		if (b%2 != 0):
			continue
		block = AppendZero(b)
		if (Number in block) or any(block[j] in block[:j]+block[j+1:] for j in range(3)):
			continue
		Number += block
		for c in range(1000):
			if (c%3 != 0):
				continue
			block = AppendZero(c)
			if (Number[-2:] != block[:2]) or (block[2] in Number):
				continue
			Number += block[2]
			for d in range(1000):
				if (d%5 != 0):
					continue
				block = AppendZero(d)
				if (Number[-2:] != block[:2]) or (block[2] in Number):
					continue
				Number += block[2]
				for e in range(1000):
					if (e%7 != 0):
						continue
					block = AppendZero(e)
					if (Number[-2:] != block[:2]) or (block[2] in Number):
						continue
					Number += block[2]
					for f in range(1000):
						if (f%11 != 0):
							continue
						block = AppendZero(f)
						if (Number[-2:] != block[:2]) or (block[2] in Number):
							continue
						Number += block[2]
						for g in range(1000):
							if (g%13 != 0):
								continue
							block = AppendZero(g)
							if (Number[-2:] != block[:2]) or (block[2] in Number):
								continue
							Number += block[2]
							for h in range(1000):
								if (h%17 != 0):
									continue
								block = AppendZero(h)
								if (Number[-2:] != block[:2]) or (block[2] in Number):
									continue
								Number += block[2]
								print(Number)
								Number = Number[:-1]
							Number = Number[:-1]
						Number = Number[:-1]
					Number = Number[:-1]
				Number = Number[:-1]
			Number = Number[:-1]
		Number = Number[:-3]
	Number = Number[:-1]
"""
print (time() - StartTime, 'seconds')
