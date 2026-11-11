# ============================================================
# Problem: Travelling Cost  (buoi8)
# Source: competitive programming
# ============================================================
# Given a weighted undirected graph with n edges, a source node u,
# and q queries each asking for the shortest path from u to v.
# Print "NO PATH" if unreachable.
#
# Input:
#   - Line 1: n (edges)
#   - Next n lines: src dst w
#   - Line: u (source)
#   - Line: q (queries)
#   - Next q lines: v
#
# Output:
#   For each query: shortest distance or "NO PATH".
#
# Approach:
#   Dijkstra from source u, answer all queries from precomputed distances.
# ============================================================

import heapq


def solve():
    n = int(input())
    graph = [[] for _ in range(501)]

    for _ in range(n):
        s, d, w = map(int, input().split())
        graph[s].append((d, w))
        graph[d].append((s, w))

    u = int(input())

    INF = float('inf')
    dist = [INF] * 501
    dist[u] = 0
    heap = [(0, u)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for v, w in graph[node]:
            if dist[node] + w < dist[v]:
                dist[v] = dist[node] + w
                heapq.heappush(heap, (dist[v], v))

    q = int(input())
    for _ in range(q):
        v = int(input())
        if dist[v] == INF:
            print("NO PATH")
        else:
            print(dist[v])


if __name__ == "__main__":
    solve()
