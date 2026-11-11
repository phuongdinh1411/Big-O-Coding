# ============================================================
# Problem: Median  (buoi7)
# Source: competitive programming
# ============================================================
# Given n numbers, find the median (middle value when sorted).
# If n is odd, the median is the middle element.
# If n is even, the median is the lower-middle element.
#
# Input:
#   - Line 1: n
#   - Line 2: n integers
#
# Output:
#   The median value.
#
# Approach:
#   Sort and pick index n//2 (0-indexed) for odd n, or (n-1)//2 for even.
#   The C++ code uses index i that starts at 0 and increments by 1 for every
#   j that increments by 2, effectively giving index n//2.
# ============================================================

def solve():
    n = int(input())
    a = sorted(map(int, input().split()))
    print(a[n // 2])


if __name__ == "__main__":
    solve()
