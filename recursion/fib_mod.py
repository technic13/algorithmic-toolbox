# Uses python3
import sys


def fib_mod(n, m):
    period = [0, 1]
    fib_mod1 = 1    
    fib_mod2 = 0
    while True:
        t = fib_mod1
        fib_mod1 = (fib_mod1 + fib_mod2) % m
        fib_mod2 = t
        period.append(fib_mod1)
        if period[-2] == 0 and period[-1] == 1:
            break
    return period[n % (len(period) - 2)]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fib_mod(n, m))
