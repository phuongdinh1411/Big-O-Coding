# ============================================================
# Problem: Graph Connectivity  (buoi16)
# Source: UVA
# ============================================================
# Given edges between uppercase letter nodes (A to some letter),
# count the number of connected components among nodes A through
# the given maximum letter.
#
# Input:
#   - Line 1: n (test cases)
#   - Each test case:
#       - Line 1: max_letter (e.g., 'F' means nodes A-F)
#       - Next lines: two-letter strings "XY" (edge between X and Y)
#       - Blank line ends each test case.
#
# Output:
#   Number of connected components. Blank lines between cases.
#
# Approach:
#   Union-Find on 26 letters. Count roots within range [A, max_letter].
# ============================================================

import sys


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
    lines = sys.stdin.read().split('\n')
    idx = 0
    n = int(lines[idx]); idx += 1
    first = True

    for _ in range(n):
        while idx < len(lines) and not lines[idx].strip():
            idx += 1

        max_letter = lines[idx].strip(); idx += 1
        limit = ord(max_letter) - 65

        parent = list(range(26))
        rank = [0] * 26

        while idx < len(lines) and lines[idx].strip():
            edge = lines[idx].strip(); idx += 1
            if len(edge) >= 2:
                union(parent, rank, ord(edge[0]) - 65, ord(edge[1]) - 65)

        idx += 1  # skip blank line

        count = sum(1 for i in range(limit + 1) if find(parent, i) == i)

        if not first:
            print()
        first = False
        print(count)


if __name__ == "__main__":
    solve()
