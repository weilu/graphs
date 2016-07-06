#Uses python3

import sys


def explore(v, adj, visited, post_order, count):
    visited.add(v)
    for w in adj[v]:
        if w not in visited:
            explore(w, adj, visited, post_order, count)
    post_order[v] = count[0]
    count[0] += 1

def acyclic(adj):
    visited = set()
    post_order = [0] * len(adj)
    count = [0] # use an array because int references by value
    for v in range(0, len(adj)):
        if v not in visited:
            explore(v, adj, visited, post_order, count)
    # v -> w, w should have a smaller post order for it to be a DAG
    for v in range(0, len(adj)):
        for w in adj[v]:
            if post_order[v] < post_order[w]:
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
