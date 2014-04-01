import itertools
import copy
import time

StartTime = time.time()
"""
#My first approach - was too unefficient, it worked by prime factorization, permutation of prime factors for getting 
#proper divisors, and checking by this way if a number is abundant. Then checking all numbers up to limit for abundancy-
#Eratosthenes Sieve - finds all prime numbers up to a limit, returns them as list 'primes'
limit = 170 # upper limit for numbers to be searched for primes
primes = [2, 3]
num2check = [True] * ((limit//2)-1)
while True in num2check:
  x = num2check.index(True)
  y = x*2 + 5
  primes.append(y)
  for i in range((x), len(num2check), y):
    num2check[i] = False
#
pfdict = dict() # dictionary where prime factors for numbers get saved

#primeFactors - returns a list of prime factors for a given integer x
def GetPrimeFactors(x):
  pf = list()
  if x in pfdict:
    for i in pfdict.get(x):
      pf.append(i)
  elif x == 1:
    pf.append(1)
    pfdict.update({x:pf})
  else:
    y = copy.deepcopy(x)
    for i in primes:
      if x % i == 0:
        while x % i ==0:
          x = x / i
          pf.append(i)
      if x == 1:
        break
      if x in pfdict:
        for j in pfdict.get(x):
          pf.append(j)
        break
    pfdict.update({y:pf})
  return(pf)


#list of proper divisors
def GetProperDivisors(x):
  #pf = pfdict[x] 
  pf =  GetPrimeFactors(x)
  dmap = list()
  indices = list()
  for i in range(len(pf)):
    indices.append(i)
  for i in range(1, len(pf)+1):
    submap = itertools.permutations(indices, i)
    for j in submap:
      dmap.append(j)
  lopd = list()
  for i in dmap:
    nd = 1
    for j in i:
      nd = nd * pf[j]
    if nd not in lopd and nd != x:
      lopd.append(nd)
  lopd.append(1)
  lopd.sort()
  return(lopd)

#check integer for abundancy
def AbundancyCheck(x):
	Abundancy = False # considering numbers as not abundant by default
	ProperDivisors = GetProperDivisors(x) #start with a list of proper divisors
	if sum(ProperDivisors) > x: # If sum of proper divisors is larger than the number, number is abundant
		Abundancy = True
	return Abundancy

#check all numbers up to limit for Abundancy:
AbundantNumbers = []
for i in range(1,10000): # program hangs when starting with 0, i.e. omitting start of range
	if AbundancyCheck(i):
		AbundantNumbers.append(i)
#check, which numbers can not be written as sum of two abundant numbers
print(AbundantNumbers)
"""

#Second Approach:  Iterating through every number up to limit, if the number is a divisor of another number under limit, the divisor gets added to the array with sums of proper divisors
limit = 30000

SumsOfDivisors = limit*[0] # Array for the sum of proper divisors for all numbers up to limit, initialized with 0's
AbundantNumbers = []
for i in range(1,limit):
	for j in range(2*i,limit,i):
		SumsOfDivisors[j-1] = SumsOfDivisors[j-1] + i

#checking for abundant numbers, if number is abundant add to list
for i in range(limit):
	if SumsOfDivisors[i]>(i+1):
		AbundantNumbers.append(i+1)

NumbersCheck = limit * [True] #Array which contains a True for every number that can not be expressed as sum of 2 abundant ones, initialized with True
#Set boolean to False if Number can be expressed as sum of 2 abundant ones
for i in range(len(AbundantNumbers)):
	for j in range(i,len(AbundantNumbers)):
		a,b = AbundantNumbers[i], AbundantNumbers[j]
		if (a+b) <= limit:
			NumbersCheck[a+b-1] = False

#parse through boolean array, if True(stands for Number which can not be expressed as sum of 2 abundant ones) add index(=number) to result list
Numbers = []
for i in range(len(NumbersCheck)):
	if NumbersCheck[i]:
		Numbers.append(i+1)
print(sum(Numbers))
print ( time.time() -StartTime ), "seconds"

#RunTime: limit=30000:12s

