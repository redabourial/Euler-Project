def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


n = 20
print(int(factorial(n*2)/(factorial(n)**2)))
