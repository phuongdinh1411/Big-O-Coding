# ============================================================
# Problem: Ubiquitous Religions  (final)
# Source: UVA
# ============================================================
# n students each practice at most 2 religions. Given m observations
# "student i and student j share the same religion", find the maximum
# number of different religions.
#
# Input:
#   - Multiple test cases until "0 0".
#   - Each test case:
#       - Line 1: n m (students, observations)
#       - Next m lines: i j (i and j share a religion)
#
# Output:
#   "Case X: R" where R is the maximum number of distinct religions.
#
# Approach:
#   Union-Find. Initially each student is their own religion.
#   After all unions, count distinct roots.
# ============================================================

def solve():
    case = 0
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        case += 1

        parent = list(range(n + 1))
        rank = [0] * (n + 1)

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
            if rank[pa] == rank[pb]:
                rank[pa] += 1

        for _ in range(m):
            i, j = map(int, input().split())
            union(i, j)

        religions = sum(1 for i in range(1, n + 1) if find(i) == i)
        print(f"Case {case}: {religions}")


if __name__ == "__main__":
    solve()
