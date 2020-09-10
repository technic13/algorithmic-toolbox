def fib_sum_last_digit(n):
    period = [0, 1]
    fib_mod1 = 1    
    fib_mod2 = 0
    while True:
        t = fib_mod1
        fib_mod1 = (fib_mod1 + fib_mod2) % 10
        fib_mod2 = t
        period.append(fib_mod1 ** 2)
        if period[-2] == 0 and period[-1] == 1:
            period = period[:-2]
            break
    last_digit = ((sum(period) % 10) * (n // len(period))) % 10
    for i in range((n % len(period)) + 1):
        last_digit = (last_digit + period[i]) % 10
    return last_digit


n = int(input())
print(fib_sum_last_digit(n))
