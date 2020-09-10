import sys


def compute_min_refills(distance, tank, stops):
    stops = [0] + stops + [distance]
    counter = 0
    fuel = tank
    for i in range(1, len(stops)):
        cur_dist = stops[i] - stops[i - 1]
        if cur_dist > tank:
            return -1
        if cur_dist > fuel:
            fuel = tank
            counter += 1
        fuel -= cur_dist
    return counter


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
