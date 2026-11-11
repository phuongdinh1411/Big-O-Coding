# ============================================================
# Problem: Cobbled Streets  (buoi15)
# Source: competitive programming
# ============================================================
# Given t test cases, each with p (paving cost per unit of MST),
# n nodes, m edges, find the minimum total paving cost = p * MST_weight.
#
# Input:
#   - Line 1: t
#   - Each test case:
#       - Line 1: p n m
#       - Next m lines: a b c (edge from a to b with weight c)
#
# Output:
#   Minimum paving cost for each test case.
#
# Approach:
#   Prim's MST algorithm. Total cost = MST weight * p.
# ============================================================

import heapq


def prim_mst(n, graph):
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

    return total


def solve():
    t = int(input())
    for _ in range(t):
        p, n, m = map(int, input().split())
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))
            graph[b].append((a, c))

        mst_cost = prim_mst(n, graph)
        print(mst_cost * p)


if __name__ == "__main__":
    solve()
