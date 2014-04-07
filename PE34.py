# Number can have at most 7 digits, as for 9999999 (8 digits) the sum of factorials of all digits only has 7 digits
#28.7s for total bruteforce with upper limit = 10M

from time import time
from math import factorial

StartTime = time()

Limit = 10000000
Sum = 0
Count = 0

for i in range(3, Limit):
	if sum([factorial(int(j)) for j in str(i)]) == i:
		Count += 1
		Sum += i

print(Count, 'Numbers counted')
print('Sum is',Sum)

print(time() - StartTime, 'seconds')
