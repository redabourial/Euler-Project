number = 600851475143
i = 2
while i<= number:
    if number%i == 0:
        largest_prime = i
        number = int(number/i)
    i+=1
print(largest_prime)