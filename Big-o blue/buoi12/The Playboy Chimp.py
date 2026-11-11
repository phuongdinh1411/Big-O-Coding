# ============================================================
# Problem: The Playboy Chimp  (buoi12)
# Source: UVA
# ============================================================
# Given a sorted list of chimp heights and q queries, for each queried
# height h find:
#   - The largest height in the list strictly less than h (or 'X' if none).
#   - The smallest height in the list strictly greater than h (or 'X' if none).
#
# Input:
#   - Line 1: n
#   - Line 2: n sorted integers
#   - Line 3: q
#   - Next q lines: one integer each
#
# Output:
#   For each query: "low high" on one line.
#
# Approach:
#   Binary search: lower_bound and upper_bound.
# ============================================================

import bisect


def solve():
    n = int(input())
    heights = list(map(int, input().split()))
    q = int(input())

    for _ in range(q):
        h = int(input())

        # Strictly less than h: largest such
        lo_idx = bisect.bisect_left(heights, h) - 1
        # Strictly greater than h: smallest such
        hi_idx = bisect.bisect_right(heights, h)

        lo = 'X' if lo_idx < 0 else heights[lo_idx]
        hi = 'X' if hi_idx >= n else heights[hi_idx]

        print(lo, hi)


if __name__ == "__main__":
    solve()
