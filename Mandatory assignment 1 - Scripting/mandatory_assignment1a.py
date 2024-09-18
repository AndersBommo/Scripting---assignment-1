# Part A

########### ORIGINAL FUNCTION ###########
"""
def find_prime_factors(n, prime_factor=[]):
    i =2 
    while i*i <=0:
        if n%i ==0:
            prime_factor.append(i)
            n//=i
        else:
            i += 1
    if n> 1: 
        prime_factor.append(n)
    return prime_factor
"""
########### BUGS REMOVED ###########
"""def find_prime_factors(n):
    
    prime_factors = []
        
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

user = int(input("Enter a number: "))

print(find_prime_factors(user))"""


########### OPTIMIZED FUNCTION ###########
def find_prime_factors(n):
    prime_factors = []

    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n //= i
        i += 2 

    if n > 2:
        prime_factors.append(n)

    return prime_factors

user = int(input("Enter a number: "))

print(find_prime_factors(user))