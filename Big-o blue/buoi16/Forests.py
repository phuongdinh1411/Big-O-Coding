# ============================================================
# Problem: Forests  (buoi16)
# Source: UVA
# ============================================================
# Given p plants and t tests, each plant has a result for each test (1/0).
# Two plants are "compatible" if for every test, they have the same result
# (or at least one has 0 — actually: neither has a conflicting result).
# More precisely: compatible if for all tests, NOT (one=1 and other=0) AND NOT (one=0 and other=1).
# i.e., for each test k: plant_i[k] == plant_j[k] OR one of them is 0.
# Wait, re-reading: compatible if row_i and row_j agree on all tests
# (both 0 or both 1 for every test they both participated in).
# Count the number of connected components using Union-Find.
#
# Input:
#   - Line 1: n (test cases)
#   - Each test case:
#       - Line 1: p t
#       - Next lines: "plant test" pairs until blank line
#
# Output:
#   Number of groups, with blank lines between cases.
#
# Approach:
#   Build membership matrix. Unite plants that are compatible (share all tests consistently).
#   Count Union-Find components.
# ============================================================

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1


def solve():
    import sys
    lines = sys.stdin.read().split('\n')
    idx = 0
    n = int(lines[idx]); idx += 1
    first = True

    for _ in range(n):
        p, t = map(int, lines[idx].split()); idx += 1

        membership = [[0] * (t + 1) for _ in range(p + 1)]

        while idx < len(lines) and lines[idx].strip():
            plant, test = map(int, lines[idx].split()); idx += 1
            membership[plant][test] = 1

        idx += 1  # skip blank line

        parent = list(range(p + 1))
        rank = [0] * (p + 1)

        for i in range(1, p + 1):
            for j in range(i + 1, p + 1):
                compatible = all(
                    not (membership[i][k] == 1 and membership[j][k] == 0) and
                    not (membership[i][k] == 0 and membership[j][k] == 1)
                    for k in range(1, t + 1)
                )
                if compatible:
                    union(parent, rank, i, j)

        components = sum(1 for i in range(1, p + 1) if find(parent, i) == i)

        if not first:
            print()
            print()
        first = False
        print(components)


if __name__ == "__main__":
    solve()
