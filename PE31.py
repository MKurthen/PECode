#15.6s
from time import time

StartTime = time()

coins = [1,2,5,10,20,50,100]
count = 1 # 1 way (one 2pound coin) excluded from algorithm
for a in range(3):
	for b in range(5):
		for c in range(11):
			for d in range(21):
				for e in range(41):
					for f in range(101):
						for g in range(201):
							amount = ((a*100) + (b*50) + (c*20)+ (d*10) + (e*5) + (f*2) + g)
							if amount == 200:
								count += 1
							if amount > 200:
								break


print((time()-StartTime) ,'seconds')
