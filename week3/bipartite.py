#Uses python3

import sys
from queue import Queue

def bfs(adj, q, dist):
    while(not q.empty()):
        cur = q.get()
        for w in adj[cur]:
            if w not in dist:
                dist[w] = dist[cur] + 1
                q.put(w)

def bipartite(adj):
    if len(adj) == 0:
        return 1

    q = Queue()
    q.put(0)
    dist = {0: 0}

    bfs(adj, q, dist)

    for v in range(1, len(adj)):
        if v not in dist:
            q.put(v)
            dist[v] = 0
            bfs(adj, q, dist)
            # dist contains dist to multiple nodes, it doesn't matter since
            # it's the two-colorable we are after

    for v in range(0, len(adj)):
        group = dist[v] % 2
        for w in adj[v]:
            if dist[w] % 2 == group:
                return 0

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
