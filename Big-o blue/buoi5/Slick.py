# ============================================================
# Problem: Slick  (buoi5)
# Source: UVA / competitive
# ============================================================
# Given an m×n binary grid (1 = oil slick, 0 = water), find all
# connected components of 1s (4-connectivity). Output:
#   - Total number of oil slick regions.
#   - For each distinct region size (ascending): "size count".
#
# Input:
#   - Multiple test cases until "0 0".
#   - Each test case:
#       - Line 1: m n
#       - Next m lines: n integers (0 or 1).
#
# Output:
#   For each test case:
#     total_regions
#     size1 count1
#     size2 count2
#     ...
#
# Approach:
#   BFS flood fill for each unvisited '1'. Count component sizes.
# ============================================================

from collections import deque, Counter


def solve():
    while True:
        line = input().split()
        m, n = int(line[0]), int(line[1])
        if m == 0:
            break

        grid = []
        for _ in range(m):
            grid.append(list(map(int, input().split())))

        visited = [[False] * n for _ in range(m)]
        sizes = []

        for si in range(m):
            for sj in range(n):
                if grid[si][sj] == 1 and not visited[si][sj]:
                    # BFS
                    queue = deque([(si, sj)])
                    visited[si][sj] = True
                    size = 1
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                size += 1
                                queue.append((nx, ny))
                    sizes.append(size)

        print(len(sizes))
        count = Counter(sizes)
        for sz in sorted(count):
            print(sz, count[sz])


if __name__ == "__main__":
    solve()
