# ============================================================
# Problem: Diving for Gold
# Source: UVA
# ============================================================
# John the diver has t seconds of air. There are n treasures at various
# depths. Diving to depth d takes w*d seconds, returning takes 2*w*d seconds,
# so total time per treasure = 3*w*d. Maximize gold collected.
# Output the items selected (in input order).
#
# Input:
#   - Multiple test cases (blank-line separated).
#   - Each test case:
#       - Line 1: t w
#       - Line 2: n
#       - Next n lines: di vi (depth and gold value)
#
# Output:
#   For each test case (blank line between cases):
#     max gold
#     number of items
#     each item: di vi  (in input order)
#
# Approach:
#   0/1 Knapsack with time capacity t. Weight = 3*w*d, value = v.
#   Track selection with full 2D DP for backtracking.
# ============================================================

import sys


def solve():
    raw = sys.stdin.read().strip().split('\n')
    idx = 0
    first = True

    while idx < len(raw):
        while idx < len(raw) and not raw[idx].strip():
            idx += 1
        if idx >= len(raw):
            break

        t, w = map(int, raw[idx].split()); idx += 1
        n = int(raw[idx]); idx += 1

        treasures = []
        for _ in range(n):
            d, v = map(int, raw[idx].split()); idx += 1
            treasures.append((d, v))

        costs = [3 * w * d for d, v in treasures]
        values = [v for d, v in treasures]

        # Full 2D DP for reconstruction
        dp = [[0] * (t + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for c in range(t + 1):
                dp[i][c] = dp[i - 1][c]
                if c >= costs[i - 1]:
                    dp[i][c] = max(dp[i][c],
                                   dp[i - 1][c - costs[i - 1]] + values[i - 1])

        # Backtrack
        selected = []
        c = t
        for i in range(n, 0, -1):
            if dp[i][c] != dp[i - 1][c]:
                selected.append(i - 1)
                c -= costs[i - 1]
        selected.reverse()

        if not first:
            print()
        first = False

        print(dp[n][t])
        print(len(selected))
        for i in selected:
            print(treasures[i][0], treasures[i][1])


if __name__ == "__main__":
    solve()
