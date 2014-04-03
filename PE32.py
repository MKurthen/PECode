#0.3s
from time import time
StartTime = time()

products =set() 
digits = {1,2,3,4,5,6,7,8,9}
for a in digits:
	digits.remove(a)
	for b in digits:
		digits.remove(b)
		for c in digits:
			digits.remove(c)
			for d in digits:
				digits.remove(d)
				for e in digits:
					digits.remove(e)
					#check 1x4 combinations
					x = a * int(str(b) + str(c) + str(d) + str(e))
					if len(str(x)) == 4:
						for i in str(x):
							if int(i) not in digits or (str(x).count(i)>1):
								break
						else:
							products.add(x)
					#check 2x3 combinations
					x = int(str(a)+str(b))* int(str(c) + str(d) + str(e))
					if len(str(x)) == 4:
						for i in str(x):
							if int(i) not in digits or (str(x).count(i)>1):
								break
						else:
							products.add(x)
					digits.add(e)
				digits.add(d)
			digits.add(c)
		digits.add(b)
	digits.add(a)

print((time()-StartTime), 'seconds')
