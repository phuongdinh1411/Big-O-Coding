# ============================================================
# Problem: Number of Islands  (buoi5)
# Source: LeetCode #200
# ============================================================
# Given an m×n grid of '1' (land) and '0' (water), count the number
# of islands. An island is a connected group of '1's connected
# horizontally or vertically.
#
# Input:
#   - Line 1: m n
#   - Next m lines: n characters ('0' or '1').
#
# Output:
#   Number of islands.
#
# Approach:
#   BFS flood fill: for each unvisited '1', start BFS and mark all
#   connected '1's as visited. Count starts = number of islands.
# ============================================================

from collections import deque


def num_islands(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                queue = deque([(i, j)])
                grid[i][j] = '2'
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                            grid[nx][ny] = '2'
                            queue.append((nx, ny))
    return count


def main():
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        row = list(input().strip())
        grid.append(row)
    print(num_islands(grid))


if __name__ == "__main__":
    main()
