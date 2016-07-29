#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    dist = [sys.maxsize for _ in range(0, len(adj))]
    dist[s] = 0

    unexplored = queue.PriorityQueue()
    unexplored.put((dist[s], s))
    explored = set()
    while not unexplored.empty():
        p, v = unexplored.get()
        if v not in explored:
            for i, w in enumerate(adj[v]):
                new_dist = cost[v][i] + dist[v]
                if dist[w] > new_dist:
                    dist[w] = new_dist
                    unexplored.put((new_dist, w))
            explored.add(v)

    return dist[t] if dist[t] < sys.maxsize else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
