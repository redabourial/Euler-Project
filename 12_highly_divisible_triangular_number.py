from math import sqrt

def get_factors_iter(n):
    for f in range(2,int(sqrt(n))+1):
        if n%f==0:
            yield f
            yield n/f

def get_factors(n):
    return list(get_factors_iter(n))

def get_triangular_numbers():
    number = 0
    index = 1
    while True:
        number+=index
        yield number
        index+=1

for triangular_number in get_triangular_numbers():
    factors = get_factors(triangular_number)
    if len(factors)> 500:
        print(triangular_number)
        exit()