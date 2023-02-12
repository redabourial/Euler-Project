def get_chain_length(n):
    chain_length = 0
    while n != 1:
        chain_length += 1
        if n % 2:
            n = 3*n+1
        else:
            n = n/2
    return chain_length

longuest_chain,number = 0,1
for n in range(2,1000*1000+1):
    chain_length = get_chain_length(n)
    if chain_length> longuest_chain:
        longuest_chain = chain_length
        number=n

print(number)