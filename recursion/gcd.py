import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b) 
    if a == 0 or b == 0:
        return max(a, b)
    while b != 0:
        a %= b
        a, b = max(a, b), min(a, b)
    return a


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
