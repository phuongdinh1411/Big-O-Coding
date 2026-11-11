# ============================================================
# Problem: King's Path
# Source: Codeforces
# ============================================================
# A king is on an infinite 10^9 × 10^9 chess board.
# Only some cells are allowed, given as n segments:
# segment i covers columns [ai, bi] in row ri.
# Total allowed cells ≤ 10^5.
# The king moves to any 8-neighbor in one step.
# Find the minimum moves from (x0,y0) to (x1,y1) through allowed cells,
# or -1 if impossible.
#
# Input:
#   - Line 1: x0 y0 x1 y1
#   - Line 2: n
#   - Next n lines: ri ai bi
#
# Output:
#   Minimum moves, or -1.
#
# Approach:
#   Store allowed cells in a set, run BFS on the sparse graph.
# ============================================================

from collections import deque


def solve():
    x0, y0, x1, y1 = map(int, input().split())
    n = int(input())

    allowed = set()
    for _ in range(n):
        r, a, b = map(int, input().split())
        for c in range(a, b + 1):
            allowed.add((r, c))

    if (x0, y0) not in allowed or (x1, y1) not in allowed:
        print(-1)
        return

    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    dist = {(x0, y0): 0}
    queue = deque([(x0, y0)])

    while queue:
        x, y = queue.popleft()
        if x == x1 and y == y1:
            print(dist[(x, y)])
            return
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if (nx, ny) in allowed and (nx, ny) not in dist:
                dist[(nx, ny)] = dist[(x, y)] + 1
                queue.append((nx, ny))

    print(-1)


if __name__ == "__main__":
    solve()
