from math import sqrt

def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def get_highest_power(n,max):
    highest_power = n
    while highest_power<=max:
        highest_power*=n
    return highest_power/n

def get_highest_powers_below(max):
    return [
        get_highest_power(n, max)
        for n in range(2,max+1)
        if is_prime(n)
    ]

powers = get_highest_powers_below(20)
answer =1 
for power in powers:
    answer*= power

print(int(answer)) 