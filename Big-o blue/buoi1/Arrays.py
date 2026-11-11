# ============================================================
# Problem: Arrays  (buoi1 / buoi2)
# Source: Codeforces
# ============================================================
# Given two sorted arrays A (size na) and B (size nb), an integer k,
# and an integer m, determine if A[k-1] < B[nb-m] (1-indexed).
# In other words: is the k-th element of A strictly less than the
# (nb-m+1)-th element of B?
# Print "YES" if true, "NO" otherwise.
#
# Input:
#   - Line 1: na nb
#   - Line 2: k m
#   - Line 3: na integers (array A)
#   - Line 4: nb integers (array B)
#
# Output:
#   "YES" or "NO"
# ============================================================

def solve():
    na, nb = map(int, input().split())
    k, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print("YES" if a[k - 1] < b[nb - m] else "NO")


if __name__ == "__main__":
    solve()
