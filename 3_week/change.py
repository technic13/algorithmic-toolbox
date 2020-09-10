import sys


def get_change(m):
    num_10 = m // 10
    m %= 10
    num_5 = m // 5
    m %= 5
    num_1 = m
    return num_1 + num_5 + num_10


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
