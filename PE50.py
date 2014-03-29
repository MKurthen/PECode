
#Eratosthenes Sieve - finds all prime numbers up to a limit, returns them as list 'primes'
limit = 1000000 # upper limit for numbers to be searched for primes
primes = [2, 3]
num2check = [True] * ((limit//2)-1)
while True in num2check:
  x = num2check.index(True)
  y = x*2 + 5
  primes.append(y)
  for i in range((x), len(num2check), y):
    num2check[i] = False
    
print(primes)



#approach:
#1. find all primes up to 1M (eratosthenes sieve to slow -> atkins sieve?
#2. parse prime numbers: begin with chain length n= 21: find longest chain of primes where the sum is prime
