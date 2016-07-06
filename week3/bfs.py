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

def distance(adj, s, t):
    q = Queue()
    q.put(s)
    dist = {s: 0}

    bfs(adj, q, dist)

    return dist[t] if t in dist else -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
