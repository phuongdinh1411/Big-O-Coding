# ============================================================
# Problem: Megacity  (buoi13)
# Source: Codeforces
# ============================================================
# The city of Novosibirsk has a current population s. There are n
# nearby towns each at some distance from the city center and with
# population p. The city can annex towns (closest first). Find the
# minimum radius to reach population >= 10^6, or -1 if impossible.
#
# Input:
#   - Line 1: n s
#   - Next n lines: x y p (coordinates and population)
#
# Output:
#   Minimum annexation radius (7 decimal places), or -1.
#
# Approach:
#   Sort towns by distance to origin. Greedily annex nearest towns
#   until population >= 10^6 or all towns exhausted.
# ============================================================

import math


def solve():
    n, s = map(int, input().split())
    towns = []
    for _ in range(n):
        x, y, p = map(int, input().split())
        dist = math.sqrt(x * x + y * y)
        towns.append((dist, p))

    towns.sort()

    for dist, p in towns:
        s += p
        if s >= 10 ** 6:
            print(f"{dist:.7f}")
            return

    print(-1)


if __name__ == "__main__":
    solve()
