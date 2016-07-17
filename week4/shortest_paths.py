#Uses python3

import sys
from queue import Queue

def _both_neg_infinity_and_negative_dist(dist_v, dist_w, edge):
    return dist_v == sys.maxsize and dist_w == sys.maxsize and edge < 0

def explore(adj, cost, dist):
    updated = set()
    for v in range(0, len(adj)):
        for i, w in enumerate(adj[v]):
            new_dist = cost[v][i] + dist[v]
            if dist[w] > new_dist and not _both_neg_infinity_and_negative_dist(distance[v], distance[w], cost[v][i]):
                dist[w] = new_dist
                updated.add(w)
    return updated

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # do Bellman-Ford v-1 times
    distance[s] = 0
    for i in range(0, len(adj)-1):
        if not explore(adj, cost, distance):
            return # no negative cycle detected early

    # do Bellman-Ford vth times & find nodes forming a negative cycles
    updated = explore(adj, cost, distance)
    for node_on_neg in updated:
        visited = set()
        dfs(adj, node_on_neg, node_on_neg, visited, shortest)

    # bfs from negative cycles nodes to find all nodes reachable from neg cycle
    # because they are also -infinite in distance
    q = Queue()
    for v, has_shortest in enumerate(shortest):
        if not has_shortest:
            q.put(v)
    bfs(adj, q, shortest)

# returns True when current node is on a cycle
def dfs(adj, start, curr, visited, shortest):
    if curr == start and visited: # do not return [] on first iteration
        return True
    visited.add(curr)
    for v in adj[curr]:
        if v == start or v not in visited:
            if dfs(adj, start, v, visited, shortest):
                shortest[v] = 0
                return True

def bfs(adj, q, shortest):
    while not q.empty():
        cur = q.get()
        for w in adj[cur]:
            if shortest[w]:
                shortest[w] = 0
                q.put(w)


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

