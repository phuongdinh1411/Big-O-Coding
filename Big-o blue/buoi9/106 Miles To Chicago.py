# ============================================================
# Problem: 106 Miles to Chicago  (buoi9)
# Source: UVA
# ============================================================
# Given a graph of n cities and m bidirectional roads, each road with
# a probability p of being safe, find the maximum probability path
# from city 1 to city n. The path probability = product of edge probabilities.
#
# Input:
#   - Multiple test cases until n = 0.
#   - Each test case:
#       - Line 1: n
#       - Line 2: m
#       - Next m lines: a b p  (cities and probability 0-100)
#
# Output:
#   "X.XXXXXX percent" for each test case.
#
# Approach:
#   Modified Bellman-Ford/Dijkstra maximizing product.
#   Use Bellman-Ford with maximization: prob[v] = max(prob[v], prob[u]*edge_p).
# ============================================================

def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        m = int(input())

        edges = []
        for _ in range(m):
            parts = input().split()
            a, b, p = int(parts[0]), int(parts[1]), float(parts[2]) / 100
            edges.append((a, b, p))
            edges.append((b, a, p))

        prob = [0.0] * (n + 1)
        prob[1] = 1.0

        for _ in range(n - 1):
            for a, b, p in edges:
                if prob[a] * p > prob[b]:
                    prob[b] = prob[a] * p

        print(f"{prob[n] * 100:.6f} percent")


if __name__ == "__main__":
    solve()
