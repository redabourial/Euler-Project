answer = sum([
    i for i in range(10000)
    if i % 5 == 0 or i % 3 == 0
])

print(answer)