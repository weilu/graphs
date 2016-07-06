#Uses python3

import sys

def explore(v, adj, visited, ccnum, cc):
    visited.add(v)
    ccnum[v] = cc
    for w in adj[v]:
        if w not in visited:
            explore(w, adj, visited, ccnum, cc)

def number_of_components(adj):
    visited = set()
    ccnum = {}
    cc = 0
    for v in range(0, len(adj)):
        if v not in visited:
            explore(v, adj, visited, ccnum, cc)
            cc += 1
    return cc

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
    print(number_of_components(adj))
