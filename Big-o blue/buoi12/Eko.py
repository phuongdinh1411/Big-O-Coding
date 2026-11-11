# ============================================================
# Problem: Eko  (buoi12)
# Source: SPOJ
# ============================================================
# n trees have heights. A lumberjack sets a saw height H; every tree
# taller than H gets cut to H (the excess falls). Find the maximum H
# such that at least m meters of wood are collected.
#
# Input:
#   - Line 1: n m
#   - Line 2: n tree heights
#
# Output:
#   Maximum H (integer).
#
# Approach:
#   Binary search on H. For a given H, total wood = sum(max(0, t-H) for t in trees).
#   Find maximum H where total >= m.
# ============================================================

def solve():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    left, right = 0, max(trees)
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        total = sum(max(0, t - mid) for t in trees)

        if total >= m:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    print(ans)


if __name__ == "__main__":
    solve()
