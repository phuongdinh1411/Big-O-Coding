# ============================================================
# Problem: Wormholes  (buoi9)
# Source: UVA / Kattis
# ============================================================
# Given a directed graph with v vertices and e edges (possibly negative
# weights), determine if a negative-weight cycle exists.
# (Wormholes = edges with negative weight that could allow time travel.)
#
# Input:
#   - Line 1: n (test cases)
#   - Each test case:
#       - Line 1: v e
#       - Next e lines: a b c (directed edge, weight c)
#
# Output:
#   "possible" if negative cycle exists, "not possible" otherwise.
#
# Approach:
#   Bellman-Ford from node 0. If any edge can still be relaxed after
#   v-1 iterations, a negative cycle exists.
# ============================================================

def solve():
    n = int(input())
    for _ in range(n):
        v, e = map(int, input().split())
        edges = []
        for _ in range(e):
            a, b, c = map(int, input().split())
            edges.append((a, b, c))

        INF = float('inf')
        dist = [INF] * v
        dist[0] = 0

        for _ in range(v - 1):
            for a, b, c in edges:
                if dist[a] != INF and dist[a] + c < dist[b]:
                    dist[b] = dist[a] + c

        # Check for negative cycle
        neg_cycle = False
        for a, b, c in edges:
            if dist[a] != INF and dist[a] + c < dist[b]:
                neg_cycle = True
                break

        print("possible" if neg_cycle else "not possible")


if __name__ == "__main__":
    solve()
