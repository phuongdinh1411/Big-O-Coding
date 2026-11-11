# ============================================================
# Problem: The Shortest Path  (buoi8)
# Source: UVA / competitive
# ============================================================
# Given s scenarios. Each scenario has n named cities, each city has
# p bidirectional roads to other cities (by number, with cost).
# Then r queries: shortest path between two named cities.
#
# Input:
#   - Line 1: s
#   - Each scenario:
#       - Line 1: n (cities)
#       - Next n lines: name p  then p pairs: neighbor cost
#       - Line: r (queries)
#       - Next r lines: name1 name2
#
# Output:
#   For each query: shortest path distance.
#
# Approach:
#   Dijkstra's algorithm per scenario. Map names to integer IDs.
# ============================================================

import heapq


def dijkstra(graph, src, n):
    dist = [float('inf')] * (n + 1)
    dist[src] = 0
    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


def solve():
    s = int(input())
    for _ in range(s):
        n = int(input())
        name_map = {}
        graph = [[] for _ in range(n + 1)]
        idx = 1

        for _ in range(n):
            parts = input().split()
            name = parts[0]
            p = int(parts[1])
            name_map[name] = idx
            for k in range(p):
                nb = int(parts[2 + 2 * k])
                cost = int(parts[3 + 2 * k])
                graph[idx].append((nb, cost))
                graph[nb].append((idx, cost))
            idx += 1

        r = int(input())
        for _ in range(r):
            a, b = input().split()
            src = name_map[a]
            dst = name_map[b]
            dist = dijkstra(graph, src, n)
            print(dist[dst])


if __name__ == "__main__":
    solve()
