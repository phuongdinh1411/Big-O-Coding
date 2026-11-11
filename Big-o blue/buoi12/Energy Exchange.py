# ============================================================
# Problem: Energy Exchange  (buoi12)
# Source: Codeforces
# ============================================================
# n accumulators with current charge levels. Accumulators above level x
# give energy to those below x. Energy transfer has k% loss.
# Find the maximum x such that all accumulators can reach level x
# (givers can fully supply receivers accounting for k% loss).
#
# Input:
#   - Line 1: n k
#   - Line 2: n integers (charge levels, 0-1000)
#
# Output:
#   Maximum x with 7 decimal places.
#
# Approach:
#   Binary search on x. For given x:
#     give = sum((a - x) * (1 - k/100)) for a > x
#     receive = sum(x - a) for a < x
#   Valid if give >= receive.
# ============================================================

def solve():
    n, k = map(int, input().split())
    acc = list(map(int, input().split()))

    left, right = 0.0, 1000.0
    ans = 0.0

    for _ in range(100):
        mid = (left + right) / 2
        give = sum((a - mid) * (1 - k / 100) for a in acc if a > mid)
        receive = sum(mid - a for a in acc if a < mid)

        if give >= receive:
            ans = mid
            left = mid
        else:
            right = mid

    print(f"{ans:.7f}")


if __name__ == "__main__":
    solve()
