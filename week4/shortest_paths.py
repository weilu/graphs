#Uses python3

import sys
import queue

def explore(adj, cost, dist):
    updated = set()
    for v in range(0, len(adj)):
        for i, w in enumerate(adj[v]):
            new_dist = cost[v][i] + dist[v]
            if dist[w] > new_dist:
                dist[w] = new_dist
                updated.add(w)
    return updated

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    for i in range(0, len(adj)-1):
        if not explore(adj, cost, distance):
            break
    updated = explore(adj, cost, distance)
    print(updated)
    for node_on_neg in updated:
        visited = set()
        dfs(adj, node_on_neg, node_on_neg, visited, shortest)
        print(shortest)

# returns True when current node is on a cycle
def dfs(adj, start, curr, visited, shortest):
    if curr == start and visited: # do not return [] on first iteration
        return True
    visited.add(curr)
    for v in adj[curr]:
        print('v: {} shortest[v]: {}'.format(v, shortest[v]))
        if v == start or v not in visited:
            if dfs(adj, start, v, visited, shortest):
                shortest[v] = 0
                return True


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
    s = data[0]
    s -= 1
    distance = [sys.maxsize] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if shortest[x] == 0:
            print('-')
        else:
            print(distance[x] if distance[x] < sys.maxsize else '*')

