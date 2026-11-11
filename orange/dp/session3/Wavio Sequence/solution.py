# ============================================================
# Problem: Wavio Sequence
# Source: UVA
# ============================================================
# A Wavio sequence has:
#   - Odd length L = 2k+1
#   - First k+1 elements strictly increasing
#   - Last k+1 elements strictly decreasing
#   - The peak element is shared between both halves
# Find the length of the longest Wavio subsequence.
#
# Input:
#   - Multiple test cases until EOF.
#   - Each test case:
#       - Line 1: N (1 ≤ N ≤ 10000)
#       - Lines with N integers.
#
# Output:
#   For each test case: length of longest Wavio subsequence.
#
# Approach:
#   For each index i as the peak:
#     LIS[i] = LIS ending at i (from left)
#     LDS[i] = LDS starting at i (from right, treated as LIS)
#     Wavio = 2 * min(LIS[i], LDS[i]) - 1
#   Compute LIS and LDS with O(n log n) binary search.
# ============================================================

import bisect
import sys


def compute_lis(arr):
    n = len(arr)
    lis = [0] * n
    tails = []
    for i in range(n):
        pos = bisect.bisect_left(tails, arr[i])
        lis[i] = pos + 1
        if pos == len(tails):
            tails.append(arr[i])
        else:
            tails[pos] = arr[i]
    return lis


def solve():
    data = sys.stdin.read().split()
    idx = 0
    while idx < len(data):
        n = int(data[idx]); idx += 1
        arr = [int(data[idx + i]) for i in range(n)]; idx += n

        lis = compute_lis(arr)
        lds = compute_lis(arr[::-1])[::-1]

        result = max(2 * min(lis[i], lds[i]) - 1 for i in range(n))
        print(result)


if __name__ == "__main__":
    solve()
