# ============================================================
# Problem: Philosopher's Stone
# Source: SPOJ
# ============================================================
# Harry is in an h×w chamber. Each cell contains some philosopher's stones.
# He starts at any cell in the first row and moves to the last row,
# collecting stones. From cell (i,j) he can move to:
#   (i+1, j-1),  (i+1, j),  or  (i+1, j+1)   (diagonal down or straight).
# Maximize total stones collected.
#
# Input:
#   - T test cases.
#   - Each test case:
#       - Line 1: h w
#       - Next h lines: w integers (stones per cell).
#
# Output:
#   For each test case, the maximum stones Harry can collect.
#
# Approach:
#   dp[j] = max stones reachable at column j in the current row.
#   Transition uses the previous row's values.
# ============================================================

def solve():
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        stones = [list(map(int, input().split())) for _ in range(h)]

        prev = stones[0][:]

        for i in range(1, h):
            curr = [0] * w
            for j in range(w):
                best = prev[j]
                if j > 0:
                    best = max(best, prev[j - 1])
                if j < w - 1:
                    best = max(best, prev[j + 1])
                curr[j] = stones[i][j] + best
            prev = curr

        print(max(prev))


if __name__ == "__main__":
    solve()
