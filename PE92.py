#66.2s
from time import time

StartTime = time()

count = 0
count89 = 0
count1 = 0
NumbersTo89 = {89}
NumbersTo1 = {1}
for x in range(1, 10000000):
	if x % 100000 == 0:
		print(x)
	NumbersSoFar = set()
	NumbersSoFar.add(x)
	NotSeenBefore = True	
	StrX = str(x)
	while NotSeenBefore:
		y = 0
		for i in StrX:
			y += (int(i)**2)
		if y in NumbersTo89:
			count89 += 1
			NotSeenBefore=False 
			#add all Numbers were iterated so Far for starting number x to set with Numbers leading to 89
			#NumbersTo89 = NumbersTo89.union(NumbersSoFar) #creating a union seems to take longer than looping over all numbers In NumbersSoFar and adding each one
			for i in NumbersSoFar:
				NumbersTo89.add(i)
		if y in NumbersTo1:
			count1 += 1
			NotSeenBefore=False
			#add all Numbers were iterated so Far for starting number x to set with Numbers leading to 1
			#NumbersTo1 = NumbersTo1.union(NumbersSoFar) 
			for i in NumbersSoFar:
				NumbersTo1.add(i)
		StrX = str(y)
		NumbersSoFar.add(y)


print((time()-StartTime) ,'seconds')
