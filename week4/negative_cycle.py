#Uses python3

import sys

def explore(adj, cost, dist):
    updated = False
    for v in range(0, len(adj)):
        for i, w in enumerate(adj[v]):
            new_dist = cost[v][i] + dist[v]
            if dist[w] > new_dist:
                dist[w] = new_dist
                updated = True
    return updated

def negative_cycle(adj, cost):
    dist = [sys.maxsize for _ in range(0, len(adj))]
    dist[0] = 0
    has_negative_cycle = True
    for i in range(0, len(adj)):
        if not explore(adj, cost, dist):
            has_negative_cycle = False
            break
    return 1 if has_negative_cycle else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
