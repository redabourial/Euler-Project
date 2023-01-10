fibonnacci_numbers = [1,2]
while fibonnacci_numbers[-1]<4*1000*1000:
    fibonnacci_numbers.append(
        fibonnacci_numbers[-1]+fibonnacci_numbers[-2]
    )
even_fibonnacci_numbers = [n for n in fibonnacci_numbers if n%2==0]
print(sum(even_fibonnacci_numbers))