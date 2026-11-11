# ============================================================
# Problem: Freckles  (final)
# Source: UVA
# ============================================================
# Given n freckles (points in 2D space), find the minimum total ink
# needed to connect all freckles with line segments (Minimum Spanning Tree
# of points using Euclidean distances).
#
# Input:
#   - Line 1: t (test cases)
#   - Each test case:
#       - Line 1: n
#       - Next n lines: x y (floating point coordinates)
#   - Blank line between test cases in output.
#
# Output:
#   MST total length (2 decimal places). Blank line between cases.
#
# Approach:
#   Prim's algorithm on the complete graph of Euclidean distances.
# ============================================================

import heapq
import math


def solve():
    t = int(input())
    for case in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(float, input().split())
            points.append((x, y))

        dist = [float('inf')] * n
        visited = [False] * n
        dist[0] = 0
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
                    dx = points[u][0] - points[v][0]
                    dy = points[u][1] - points[v][1]
                    d = math.sqrt(dx * dx + dy * dy)
                    if d < dist[v]:
                        dist[v] = d
                        heapq.heappush(heap, (d, v))

        print(f"{total:.2f}")
        if case < t - 1:
            print()


if __name__ == "__main__":
    solve()
