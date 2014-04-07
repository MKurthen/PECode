import numpy as np
import matplotlib.pyplot as plt
from time import time
from copy import deepcopy

StartTime = time()

NotLychrelLevel = list(range(1,50))
NotLychrelNumberStat = [0] * 49
LychrelCount = 0
LychrelNumbers = [] 

for n in range(1,10000):
	i = deepcopy(n)
	if i % 50 == 0:
		print(i)
	for j in range(49):
		i = i + int(str(i)[::-1])	
		if all(str(i)[k] == str(i)[-(k+1)] for k in range((len(str(i))//2)+1)):
			NotLychrelNumberStat[j] += 1
			break
	else:
		LychrelNumbers.append(n)
		LychrelCount += 1

print(LychrelCount, 'Lychrel Numbers below 10k')

print(time() - StartTime, 'seconds')


plt.subplot(2, 1, 1)
plt.bar(NotLychrelLevel, NotLychrelNumberStat )


plt.show()
