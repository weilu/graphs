#Uses python3
import sys
import math

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

def clustering(x, y, k):
    sets = {}
    for i, j in zip(x, y):
        v = (i, j)
        sets[v] = set()
        sets[v].add(v)

    dist = get_sorted_edges(x, y)
    results = []
    for weight, (v1, v2) in dist:
        if v2 not in sets[v1]:
            results.append(weight)
            union = sets[v1].union(sets[v2])
            for v in union:
                sets[v] = union
    return sorted(results, reverse=True)[k-2]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
