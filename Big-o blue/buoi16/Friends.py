# ============================================================
# Problem: Friends  (buoi16)
# Source: competitive programming
# ============================================================
# Given n people and m friendship pairs, find the size of the largest
# group of friends (largest connected component in the friendship graph).
#
# Input:
#   - Line 1: t (test cases)
#   - Each test case:
#       - Line 1: n m
#       - Next m lines: a b (a and b are friends, 1-indexed)
#
# Output:
#   Size of largest friend group for each test case.
#
# Approach:
#   Union-Find. Count size of each component, return max.
# ============================================================

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())

        parent = list(range(n))
        rank = [0] * n
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            size[pa] += size[pb]
            if rank[pa] == rank[pb]:
                rank[pa] += 1

        for _ in range(m):
            a, b = map(int, input().split())
            union(a - 1, b - 1)

        print(max(size[find(i)] for i in range(n)))


if __name__ == "__main__":
    solve()
