# ============================================================
# Problem: Bombs! NO they are Mines!!  (buoi5)
# Source: UVA / competitive
# ============================================================
# Given an m×n grid with some cells blocked (mines/bombs), find the
# minimum number of moves (BFS shortest path) from a start cell to
# a destination cell. Only horizontal/vertical moves allowed.
#
# Input:
#   - Multiple test cases until "0 0".
#   - Each test case:
#       - Line 1: m n
#       - Line 2: number of bomb rows
#       - For each bomb row: row_index num_bombs bomb_col1 bomb_col2 ...
#       - Last line: start_row start_col dest_row dest_col
#
# Output:
#   Minimum moves for each test case.
#
# Approach:
#   Build grid, BFS from start to destination.
# ============================================================

from collections import deque


def solve():
    while True:
        line = input().split()
        m, n = int(line[0]), int(line[1])
        if m == 0 and n == 0:
            break

        grid = [[0] * n for _ in range(m)]

        bomb_rows = int(input())
        for _ in range(bomb_rows):
            parts = list(map(int, input().split()))
            row, num = parts[0], parts[1]
            for k in range(num):
                grid[row][parts[2 + k]] = 1

        sx, sy, dx, dy = map(int, input().split())

        visited = [[False] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]
        queue = deque([(sx, sy)])
        visited[sx][sy] = True

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            if x == dx and y == dy:
                break
            for ddx, ddy in dirs:
                nx, ny = x + ddx, y + ddy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        print(dist[dx][dy])


if __name__ == "__main__":
    solve()
