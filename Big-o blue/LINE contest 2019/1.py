# ============================================================
# Problem: LINE Contest 2019 - Problem 1  (Longest Subarray Within K Difference)
# Source: LINE Contest 2019
# ============================================================
# Given n numbers and a range K, find the longest contiguous subarray
# where (max - min) <= K. (Also handle edge case with single elements.)
# For each test case output: "Case #i: length day/days"
#
# Input:
#   - Line 1: t
#   - Each test case:
#       - Line 1: n k
#       - Line 2: n integers
#
# Output:
#   "Case #i: length day" (if length==1) or "Case #i: length days"
#
# Approach:
#   Sliding window with two deques (max and min) to maintain window
#   where max - min <= k.
# ============================================================

from collections import deque


def solve():
    t = int(input())
    for i in range(1, t + 1):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        max_dq = deque()  # decreasing (front = max)
        min_dq = deque()  # increasing (front = min)
        l = 0
        best = 1

        for r in range(n):
            while max_dq and a[max_dq[-1]] <= a[r]:
                max_dq.pop()
            max_dq.append(r)

            while min_dq and a[min_dq[-1]] >= a[r]:
                min_dq.pop()
            min_dq.append(r)

            while a[max_dq[0]] - a[min_dq[0]] > k:
                l += 1
                if max_dq[0] < l:
                    max_dq.popleft()
                if min_dq[0] < l:
                    min_dq.popleft()

            best = max(best, r - l + 1)

        unit = "day" if best == 1 else "days"
        print(f"Case #{i}: {best} {unit}")


if __name__ == "__main__":
    solve()
