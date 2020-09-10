import sys


def fib_digit(n):
    f0 = 0
    f1 = 1
    for i in range(2, n+1):
        t = f0
        f0 = f1
        f1 = (f1 + t) % 10
    return f1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(fib_digit(n, m))
