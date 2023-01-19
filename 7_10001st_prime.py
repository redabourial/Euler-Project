from math import sqrt
def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

index = 0
number = 1
while index<10001:
    number+=1
    if is_prime(number):
        index+=1

print(number)