# ============================================================
# Problem: Connect the Campus  (buoi15)
# Source: UVA
# ============================================================
# Given n buildings at (x, y) coordinates, some buildings are already
# connected (given t existing connections). Find the minimum additional
# cable length needed to connect ALL buildings.
# (MST on remaining edges after accounting for existing connections.)
#
# Input:
#   - Multiple test cases until EOF.
#   - Each test case:
#       - Line 1: n
#       - Next n lines: x y
#       - Line: t (existing connections)
#       - Next t lines: b1 b2 (1-indexed)
#
# Output:
#   Minimum cable length (2 decimal places) for each test case.
#
# Approach:
#   Build complete graph with Euclidean distances. Mark existing edges
#   with cost 0 (or negative to force inclusion). Run Prim's MST.
# ============================================================

import heapq
import math


def solve():
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        buildings = []
        for _ in range(n):
            x, y = map(float, input().split())
            buildings.append((x, y))

        t = int(input())
        existing = set()
        for _ in range(t):
            a, b = map(int, input().split())
            existing.add((min(a, b), max(a, b)))

        def dist(i, j):
            dx = buildings[i][0] - buildings[j][0]
            dy = buildings[i][1] - buildings[j][1]
            return math.sqrt(dx * dx + dy * dy)

        # Prim's MST
        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        heap = [(0.0, 0)]
        total = 0.0

        while heap:
            w, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            total += w

            for v in range(n):
                if not visited[v]:
                    key = (min(u + 1, v + 1), max(u + 1, v + 1))
                    edge_cost = 0.0 if key in existing else dist(u, v)
                    if edge_cost < min_dist[v]:
                        min_dist[v] = edge_cost
                        heapq.heappush(heap, (edge_cost, v))

        print(f"{total:.2f}")


if __name__ == "__main__":
    solve()
