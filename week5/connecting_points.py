#Uses python3
import sys
import math
import queue

def get_sorted_edges(x, y):
    dist = []
    for i, j in zip(x, y):
        v1 = (i, j)
        for a, b in zip(x, y):
            v2 = (a, b)
            if v1 == v2:
                continue
            weight = math.sqrt(math.pow(i-a, 2) + math.pow(j-b, 2))
            dist.append((weight, (v1, v2)))
    return sorted(dist, key=lambda e: e[0])

def minimum_distance(x, y):
    sets = {}
    for i, j in zip(x, y):
        v = (i, j)
        sets[v] = set()
        sets[v].add(v)

    dist = get_sorted_edges(x, y)
    result = 0.
    for weight, (v1, v2) in dist:
        if v2 not in sets[v1]:
            result += weight
            union = sets[v1].union(sets[v2])
            for v in union:
                sets[v] = union
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
