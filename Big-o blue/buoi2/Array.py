# ============================================================
# Problem: Array (Two Pointers)  (buoi2)
# Source: Codeforces
# ============================================================
# Given an array of n integers and an integer k, find a subarray
# (contiguous) that contains exactly k DISTINCT values.
# Output the 1-indexed start and end positions, or "-1 -1" if none.
#
# Input:
#   - Line 1: n k
#   - Line 2: n integers
#
# Output:
#   "l r" (1-indexed) or "-1 -1"
#
# Approach:
#   Sliding window (two pointers). Expand right, shrink left when distinct
#   count reaches k. When count == k, output and stop.
# ============================================================

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = {}
    distinct = 0
    l = 0

    for r in range(n):
        freq[a[r]] = freq.get(a[r], 0) + 1
        if freq[a[r]] == 1:
            distinct += 1

        if distinct == k:
            # Shrink left to minimum valid window
            while freq[a[l]] > 1:
                freq[a[l]] -= 1
                l += 1
            print(l + 1, r + 1)
            return

    print(-1, -1)


if __name__ == "__main__":
    solve()
