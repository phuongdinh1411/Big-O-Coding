# ============================================================
# Problem: Minimum Spanning Tree  (buoi15)
# Source: competitive programming
# ============================================================
# Given n nodes and m weighted undirected edges, find the total weight
# of the Minimum Spanning Tree (MST).
#
# Input:
#   - Line 1: n m
#   - Next m lines: u v w
#
# Output:
#   MST total weight.
#
# Approach:
#   Prim's algorithm with a min-heap.
# ============================================================

import heapq


def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    total = 0

    while heap:
        w, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += w

        for v, wt in graph[u]:
            if not visited[v] and wt < dist[v]:
                dist[v] = wt
                heapq.heappush(heap, (wt, v))

    print(total)


if __name__ == "__main__":
    solve()
