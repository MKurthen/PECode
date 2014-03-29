import copy

#Eratosthenes Sieve - finds all prime numbers up to a limit, returns them as list 'primes'
limit = 1000 # upper limit for numbers to be searched for primes
primes = [2, 3]
num2check = [True] * ((limit//2)-1)
while True in num2check:
  x = num2check.index(True)
  y = x*2 + 5
  primes.append(y)
  for i in range((x), len(num2check), y):
    num2check[i] = False
print(primes)

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

primes2 = copy.deepcopy(primes)
for i in range(1,100000):
	n = (10**i)-1
	pf_n = prime_facts(n)
	for j in pf_n:
		if j in primes2:
			primes2.remove(j)	
	print(primes2)
