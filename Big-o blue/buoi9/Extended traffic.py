# ============================================================
# Problem: Extended Traffic  (buoi9)
# Source: LightOJ
# ============================================================
# Given n junctions each with a traffic value. Roads connect junctions.
# Travel cost on road (u→v) = (traffic[v] - traffic[u])^3.
# For q queries, find shortest path from junction 1 to junction q_i.
# If the path passes through a negative cycle, output "?".
# If unreachable, output "?" as well. Also output "?" if dist < 3.
#
# Input:
#   - Line 1: number of test cases
#   - Each test case:
#       - Line 1: n
#       - Line 2: n traffic values
#       - Line: m (roads)
#       - Next m lines: u v (directed road)
#       - Line: q
#       - Next q lines: destination
#
# Output:
#   "Case X:\n" then results for each query.
#
# Approach:
#   Bellman-Ford from junction 1. Mark nodes reachable via negative cycle.
#   Output "?" if unreachable, on negative cycle path, or distance < 3.
# ============================================================

def solve():
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        traffic = [0] + list(map(int, input().split()))

        m = int(input())
        roads = []
        for _ in range(m):
            u, v = map(int, input().split())
            roads.append((u, v))

        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[1] = 0

        for _ in range(n - 1):
            for u, v in roads:
                w = (traffic[v] - traffic[u]) ** 3
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Detect negative cycles
        in_neg_cycle = [False] * (n + 1)
        for _ in range(n):
            for u, v in roads:
                w = (traffic[v] - traffic[u]) ** 3
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    in_neg_cycle[v] = True
                if in_neg_cycle[u]:
                    in_neg_cycle[v] = True

        q = int(input())
        print(f"Case {case}:")
        for _ in range(q):
            dst = int(input())
            if dist[dst] == INF or in_neg_cycle[dst] or dist[dst] < 3:
                print("?")
            else:
                print(dist[dst])


if __name__ == "__main__":
    solve()
