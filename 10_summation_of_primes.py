from math import sqrt
def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True


primes = [ i for i in range(2,2*1000*1000) if is_prime(i)]
print(sum(primes))