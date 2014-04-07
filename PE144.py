# 0.06 seconds

 from Tkinter import *
from math import cos, sin, tan, sqrt, atan
from copy import deepcopy
import numpy as np
from time import time

StartTime = time()

StartCoordinates = np.array([0.0,10.1])
TargetCoordinates = np.array([1.4,-9.6])
LightBeam = np.array([TargetCoordinates[0]-StartCoordinates[0],TargetCoordinates[1]-StartCoordinates[1]]).reshape(2,1)

print('InitBeam = ', LightBeam)

master = Tk()

w = Canvas(master, width=2000, height=1000)

w.pack()

id = w.create_oval(0,0,400,800)

#define a function to draw a beam, purpose is to avoid calculation for TK Coordinates every time
def DrawBeam(x1,y1,x2,y2): 
	x1_TK = 200 + (x1 * 40)
	x2_TK = 200 + (x2 * 40)
	y1_TK = 400 - (y1 * 40)
	y2_TK = 400 - (y2 * 40)
	w.create_line(x1_TK,y1_TK,x2_TK,y2_TK,fill = 'red')
		
DrawBeam(StartCoordinates[0],StartCoordinates[1],TargetCoordinates[0],TargetCoordinates[1])

count = 0

Flag = False
while not Flag:

	count += 1
	if count > 10000:
		print 'maximum iterations exceeded, redefine Maximum'
		break

	#calculate Slope of Mirror from TargetCoordinates
	Slope = ((-4*TargetCoordinates[0])/TargetCoordinates[1])
	SlopeInRad = atan(Slope)

	#calculate ReflectionMatrix from Slope
	ReflectionMatrix = np.array([cos(2*SlopeInRad), sin(2*SlopeInRad), sin(2*SlopeInRad), -cos(2*SlopeInRad)]).reshape(2,2)

	#calculate new vector from Multiplication with ReflectionMatrix
	LightBeam = np.dot(ReflectionMatrix,LightBeam)
	StartCoordinates = deepcopy(TargetCoordinates)

	#calculate equation for Lightbeam in Form y = m*x + t
	m = float(LightBeam[1]/LightBeam[0])
	t= (StartCoordinates[1] - (StartCoordinates[0]*m))


	#calculate new target coordinates 	
		#(I)		4 x**2 + y**2 = 100
		#(II)		y = m*x + t
		#(II in I)	4 x**2 + (m*x + t)**2 = 100
		#		4 x**2 + m**2*x**2 + 2*m*x*t + t**2 = 100
		#		(4 + m**2)x**2 + (2*m*t)*x +(t**2 - 100) = 0
		#		x1,x2 = (-(2*m*t) +- sqrt(4*m**2*t**2 - 4(4+m**2)(t**2-100))) / 2(4+m**2)
		#			x1 = (-(m*t) + sqrt(400*m**2 - 16t**2 + 1600)) / (4+m**2)
		#			x2 = (-(m*t) - sqrt(400*m**2 - 16t**2 + 1600)) / (4+m**2)
	a = (4+m**2)
	b = 2*(m*t)
	c = (t**2-100)
	x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
	x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)

	#one is start, other is target, so take the further one:
	if (abs(float(StartCoordinates[0]) - x1) > abs(float(StartCoordinates[0]) - x2)):
		x = x1
	else: 
		x = x2
	y = (m*x) + t
	TargetCoordinates = np.array([x,y])
	
	#Draw reflected Beam for visualization
	DrawBeam(StartCoordinates[0],StartCoordinates[1],TargetCoordinates[0],TargetCoordinates[1])
	
	#Condition for Beam leaving cell 
	if (abs(TargetCoordinates[0]) <= 0.01) and TargetCoordinates[1] > 0:
		Flag = True
		
		
print(TargetCoordinates)
print('reflection count:', count)
print(time() - StartTime, 'seconds')



mainloop()
