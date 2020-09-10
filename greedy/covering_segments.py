import sys
from collections import namedtuple


Segment = namedtuple('Segment', 'begin end')


def optimal_points(segments):
    segments = sorted(segments, key=lambda seg: seg.end)
    points = [segments[0].end]
    for i in range(1, len(segments)):
        if not (segments[i].begin <= points[-1] <= segments[i].end):
            points.append(segments[i].end)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
