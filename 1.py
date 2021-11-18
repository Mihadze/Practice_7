def print_till_zero(n):
    if (n-1) > 0:
        print(n)
        return print_till_zero(n-1)
    elif n <= 0:
        print(n)
        return print_till_zero(n+1)
    print(1)
