# ============================================================
# Problem: Sort the Array  (buoi3)
# Source: Codeforces
# ============================================================
# Given an array of n integers, determine if it can be sorted by
# reversing exactly ONE contiguous subarray.
# If yes, print "yes" and the 1-indexed [l, r] of the subarray to reverse.
# If the array is already sorted, print "yes 1 1".
# If no single reversal works, print "no".
#
# Input:
#   - Line 1: n
#   - Line 2: n integers
#
# Output:
#   "yes\nl r"  or  "no"
#
# Approach:
#   Find the range [l, r] where a[i] != sorted_a[i].
#   Check that the subarray a[l..r] is non-increasing (reversing it gives sorted).
# ============================================================

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)

    l, r = 0, n - 1
    while l < n and a[l] == b[l]:
        l += 1
    while r >= 0 and a[r] == b[r]:
        r -= 1

    if l > r:
        print("yes")
        print(1, 1)
        return

    # Check if a[l..r] is non-increasing
    ok = all(a[i] >= a[i + 1] for i in range(l, r))
    if ok:
        print("yes")
        print(l + 1, r + 1)
    else:
        print("no")


if __name__ == "__main__":
    solve()
