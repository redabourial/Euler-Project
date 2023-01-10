def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def get_palindromic_products(end):
    for n1 in range(end,1,-1):
        for n2 in range(end,1,-1):
            n = n1*n2
            if is_palindrome(n):
                yield n1*n2

largest_palindrome = max([i for i in get_palindromic_products(999)])
print(largest_palindrome)