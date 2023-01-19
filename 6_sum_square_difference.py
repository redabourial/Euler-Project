natural_numbers = [i+1 for i in range(100)]
sum_of_squares = sum([i**2 for i in natural_numbers])
square_of_sums = sum(natural_numbers)**2
print(square_of_sums-sum_of_squares)
