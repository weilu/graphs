#Uses python3

import sys

def dfs(v, adj, visited, post_counter, order):
    visited.add(v)
    for w in adj[v]:
        if w not in visited:
            dfs(w, adj, visited, post_counter, order)
    post_counter[0] += 1
    order[len(adj) - post_counter[0]] = v


def toposort(adj):
    order = [0] * len(adj)
    visited = set()
    post_counter = [0]
    for v in range(0, len(adj)):
        if v not in visited:
            dfs(v, adj, visited, post_counter, order)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    print(' '.join(str(x + 1) for x in order))

