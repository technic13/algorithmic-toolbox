import sys


def lmc(a, b):
    a, b = max(a, b), min(a, b) 
    if a == 0 or b == 0:
        return max(a, b)
    mult = a * b
    while b != 0:
        a %= b
        a, b = max(a, b), min(a, b)
    return mult // a


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lmc(a, b))
