# ============================================================
# Problem: Guilty Prince  (buoi5)
# Source: UVA / competitive
# ============================================================
# A prince is trapped on an island represented as an n×m grid.
# Cells can be land ('.') or water ('#'). The prince starts at '@'.
# Find how many distinct land cells (including '@') the prince can reach
# by moving up/down/left/right (not diagonally).
#
# Input:
#   - Line 1: n (number of test cases)
#   - Each test case:
#       - Line 1: m rows (columns first, then rows in the C++ code → actually cols rows)
#       - Next rows lines: m characters each.
#
# Output:
#   "Case i: count" for each test case.
#
# Approach:
#   BFS from '@', count reachable '.' cells (including starting cell).
# ============================================================

from collections import deque


def solve():
    n = int(input())
    for case in range(1, n + 1):
        cols, rows = map(int, input().split())
        grid = []
        sx = sy = 0
        for i in range(rows):
            row = input().strip()
            grid.append(row)
            for j, c in enumerate(row):
                if c == '@':
                    sx, sy = i, j

        visited = [[False] * cols for _ in range(rows)]
        queue = deque([(sx, sy)])
        visited[sx][sy] = True
        count = 1  # include starting cell

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    count += 1
                    queue.append((nx, ny))

        print(f"Case {case}: {count}")


if __name__ == "__main__":
    solve()
