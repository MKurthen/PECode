from time import time
from math import sqrt, floor, ceil

StartTime = time()


def CountIntegerCoordinates(N):
	rSquare = (2*((N/2)**2)) #radius square 
	r = sqrt(rSquare) # radius
	m = float(N)/2 #center (x as well as y coordinate for center)
	
	IntegerCoordinates = list()

	# 4 integer coordinate points are provided (0,0),(0,N),(N,0),(N,N)
	count = 4

	#center of circle can only be on integer or .5, so it's sufficient to check only for x values from left to center 
	# supposing symmetry on 1/8 circles: 105 integer coordinates have to be in upper left quarter, one of them on (0,N)
		#=> 104 integer coordinate points have to be in (m-r) < x < 0
	for x in range(floor(m-r)+1,m):
		#get y coordinates from x coordinates by solving square equation of type (x-m)**2 + (y-m)**2 = r**2
		#(x-m)**2 + (y-m)**2 = r**2
		#x**2 -2xm + m**2 + y**2 -2ym + m**2 = r**2
		#y**2 -2ym +(x**2-2xm+2m**2-r**2) = 0
		a = 1
		b = -2*m
		c = (x**2 -(2*x*m) + 2*(m**2) - rSquare)
		#if y1 is integer, then y2 is integer as well (center can only be on integer or .5 value)
		y1 = (-b + sqrt(b**2 - (4*a*c)))/(2*a)
		
		if y1 % 1 == 0 or y1 % 1 == 0.0:
			count += 8
			IntegerCoordinates.append([x,y1])
			print(x,y1)
		if count > 420:
			break
	
	return count

counter = 0
"""
for i in range(1, 1000000):
	if i % 1000 == 0:
		print(i)
	n = CountIntegerCoordinates(i)
	print(i,n)
#Approach no 2: every circle goes th

"""
print(time() - StartTime, 'seconds')
