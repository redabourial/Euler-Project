

def get_possibilites(numbers_sum=1000, depth=3):
    if depth == 1:
        yield [numbers_sum]
        return
    for i in range(numbers_sum):
        for p in get_possibilites(numbers_sum=numbers_sum-i, depth=depth-1):
            yield [i]+p


for combination in get_possibilites():
    a, b, c = sorted(combination)
    if a**2+b**2 == c**2 and a != c and b != c:
        print(a * b * c)
        exit()
