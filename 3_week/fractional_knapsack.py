import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    items = sorted(list(range(len(weights))),
                   key=lambda i: values[i]/weights[i], reverse=True)
    for ind in items:
        if capacity <= 0:
            break
        cur_weight = min(capacity, weights[ind])
        value += (cur_weight / weights[ind]) * values[ind]
        capacity -= cur_weight
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
