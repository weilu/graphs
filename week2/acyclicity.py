#Uses python3

import sys


def explore(v, adj, visited, start):
    visited.add(v)
    for w in adj[v]:
        if w not in visited:
            if explore(w, adj, visited, start):
                return True
        elif w == start:
            return True
    return False

def acyclic(adj):
    visited = set()
    start = 0
    for v in range(0, len(adj)):
        if v not in visited:
            if explore(v, adj, visited, start):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
