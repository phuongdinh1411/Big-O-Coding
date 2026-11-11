# ============================================================
# Problem: Scuba Diver
# Source: SPOJ
# ============================================================
# A diver needs at least t liters of oxygen and a liters of nitrogen
# for a dive. He has n cylinders available, each with:
#   - ti liters of oxygen
#   - ai liters of nitrogen
#   - wi kg of weight
# Find the minimum total weight of cylinders satisfying both requirements.
#
# Input:
#   - c test cases (blank-line separated).
#   - Each test case:
#       - Line 1: t a (required oxygen and nitrogen)
#       - Line 2: n
#       - Next n lines: ti ai wi
#   - 1 ≤ t ≤ 21, 1 ≤ a ≤ 79, 1 ≤ n ≤ 1000
#
# Output:
#   Minimum weight for each test case.
#
# Approach:
#   2D 0/1 knapsack (minimization).
#   dp[o][n] = min weight to accumulate at least o oxygen and n nitrogen.
#   Cap state at requirements: excess doesn't help.
# ============================================================

import sys
input = sys.stdin.readline


def solve():
    c = int(input())
    for _ in range(c):
        t_req, a_req = map(int, input().split())
        n = int(input())

        INF = 10 ** 9
        dp = [[INF] * (a_req + 1) for _ in range(t_req + 1)]
        dp[0][0] = 0

        for _ in range(n):
            ti, ai, wi = map(int, input().split())

            for o in range(t_req, -1, -1):
                for ni in range(a_req, -1, -1):
                    if dp[o][ni] < INF:
                        no = min(o + ti, t_req)
                        nn = min(ni + ai, a_req)
                        dp[no][nn] = min(dp[no][nn], dp[o][ni] + wi)

        print(dp[t_req][a_req])


if __name__ == "__main__":
    solve()
