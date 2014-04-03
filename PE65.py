#0.005s
from fractions import *
from time import time

StartTime = time()

sequence =[2]
for i in range(1,34):
	sequence.append(1)
	sequence.append(2*i)
	sequence.append(1)

e = Fraction(1)
for i in range(2,len(sequence)+1):
	e = Fraction(sequence[-i]) + Fraction(1,e)
sum = 0
for i in list(str(e.numerator)):
	sum += int(i)

print(sum)
print((time()-StartTime), 'seconds')
