def power(a, n):
    if a == 0:
        print('аче всмысле')
        return False
    elif n == 0:
        return 1
    elif n % 2 != 0:
        return a * power(a, n - 1)
    else:
        return power(a, n / 2) ** 2
