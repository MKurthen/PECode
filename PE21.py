import itertools
import copy

#Eratosthenes Sieve - finds all prime numbers up to a limit, returns them as list 'primes'
limit = 10000 # upper limit for numbers to be searched for primes
primes = [2, 3]
num2check = [True] * ((limit//2)-1)
while True in num2check:
  x = num2check.index(True)
  y = x*2 + 5
  primes.append(y)
  for i in range((x), len(num2check), y):
    num2check[i] = False

pfdict = dict() # dictionary where prime factors for numbers get saved

#primeFactors - returns a list of prime factors for a given integer x
def prime_facts(x):
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

#number of divisors
def no_of_divisors(x):
  pf = prime_facts(x)
  primepowers = list()
  for i in pf:
    c = 1
    print(i)
    while pf.count(i) > 1:
      c += 1
      pf.remove(i)
    print(c)
    primepowers.append(c)
  nod = 1
  for i in primepowers:
    nod = nod*(1+i)
  return(nod)



#list of divisors
def get_lopd(x):
  pf = pfdict[x] 
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

loan = list()
lonan = list()
"""
for i in range(1, 1000):
  print(i)
  if i in primes or i in lonan or i in loan:
    continue
  # if i%2 != 0:
  #  continue
  a = get_lopd(i)
  sum_a = 0
  for j in a:
    sum_a += j
  if sum_a in lonan or sum_a in loan:
    continue
  #if sum_a % 2 != 0:
  #  lonan.append(sum_a)
  #  continue
  b = get_lopd(sum_a)
  sum_b = 0
  for j in b:
    sum_b += j
  if sum_b == i and sum_b != sum_a:
    if sum_a not in loan and sum_a not in lonan:
      loan.append(sum_a)
      loan.append(sum_b)
  else:
    lonan.append(sum_b)
    lonan.append(sum_a)
    lonan.append(i)

print(loan)
"""
#approach Euler's rule
#for n in range(1, 20):
#    for m in range(n+1,20):
#        print(n,m)
for i in range(1,10000):
	prime_facts(i)

print(get_lopd(6232))
print(sum(get_lopd(6232)))
print(get_lopd(6368))
print(sum(get_lopd(6368)))
LopdDict = dict()
	
#for i in range(1,10000):
#for i in primes:
#	LopdDict.update({i:[1,i]})
	
#for i in range(1,10000):
#	print(i)
#	lopd = get_lopd(i)
#	LopdDict.update({i:lopd})
