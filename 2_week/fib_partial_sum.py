def get_period():
    period = [0, 1]
    fib_mod1 = 1
    fib_mod2 = 0
    while True:
        t = fib_mod1
        fib_mod1 = (fib_mod1 + fib_mod2) % 10
        fib_mod2 = t
        period.append(fib_mod1)
        if period[-2] == 0 and period[-1] == 1:
            period = period[:-2]
            break
    return period


def fib_sum_last_digit(m, n):
    period = get_period()
    last_digit = 0

    for i in range(m % len(period), n % len(period) + 1):
        last_digit = (last_digit + period[i]) % 10
    intermediate_periods = n // len(period) - m // len(period)
    last_digit = (last_digit + ((sum(period) % 10) * intermediate_periods)) % 10
    return last_digit


m, n = map(int, input().split())
print(fib_sum_last_digit(m, n))
