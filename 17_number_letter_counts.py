import inflect
p = inflect.engine()

numbers = [
    p.number_to_words(i).replace("-", "").replace(" ","")
    for i in range(1, 1001)
]

print(sum([len(n) for n in numbers]))