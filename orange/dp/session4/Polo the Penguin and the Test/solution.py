# ============================================================
# Problem: Polo the Penguin and the Test
# Source: Codechef
# ============================================================
# Polo has N questions. Each question i appears in Ci tests and
# is worth Pi points per test. Learning it takes Ti minutes.
# With W minutes total, maximize the total points he can earn
# across all tests.
#
# Input:
#   - T test cases.
#   - Each test case:
#       - Line 1: N W
#       - Next N lines: Ci Pi Ti
#   - 1 ≤ T ≤ 100, 1 ≤ N,Ci,Pi,Ti ≤ 100, 1 ≤ W ≤ 100
#
# Output:
#   Maximum total points for each test case.
#
# Approach:
#   0/1 Knapsack. Each question has:
#     weight = Ti (time to learn)
#     value  = Ci * Pi (total points from all tests)
#   Capacity = W.
# ============================================================

def solve():
    t = int(input())
    for _ in range(t):
        n, w = map(int, input().split())

        dp = [0] * (w + 1)

        for _ in range(n):
            c, p, ti = map(int, input().split())
            value = c * p
            for cap in range(w, ti - 1, -1):
                dp[cap] = max(dp[cap], dp[cap - ti] + value)

        print(dp[w])


if __name__ == "__main__":
    solve()
