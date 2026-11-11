# ============================================================
# Problem: Devu, the Dumb Guy  (buoi3)
# Source: Codeforces
# ============================================================
# Devu has n bottles of milk. He drinks them in non-decreasing order
# of volume. For the i-th bottle he drinks (in sorted order), the
# pleasure is i * volume[i] (1-indexed, sorted ascending). But he can
# only perform at most x "happy-drink" operations where happiness is
# multiplied by the drink count. He wants to maximize total pleasure.
# Actually: sort, assign multipliers 1,2,...,min(x,n) to the smallest
# volumes and multiplier x to the rest.
#
# Input:
#   - Line 1: n x
#   - Line 2: n integers
#
# Output:
#   Total pleasure (sum of multiplier * volume for each bottle).
#
# Approach:
#   Sort volumes. For the i-th bottle (1-indexed):
#     multiplier = i if i ≤ x, else x.
# ============================================================

def solve():
    n, x = map(int, input().split())
    a = sorted(map(int, input().split()))

    total = 0
    for i in range(n):
        mult = min(i + 1, x)
        total += mult * a[i]

    print(total)


if __name__ == "__main__":
    solve()
