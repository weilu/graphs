#Uses python3

import sys
from toposort import toposort

sys.setrecursionlimit(200000)

def explore(v, adj, visited, cc):
    visited.add(v)
    for w in adj[v]:
        if w not in visited:
            explore(w, adj, visited, cc)

def number_of_strongly_connected_components(adj, rev_adj):
    visited = set()
    cc = 0
    order = toposort(rev_adj)
    for v in order:
        if v not in visited:
            explore(v, adj, visited, cc)
            cc += 1
    return cc

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        rev_adj[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, rev_adj))
