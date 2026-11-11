# ============================================================
# Problem: Exact Change
# Source: UVa
# ============================================================
# You want to buy an item costing P cents. You have n bills/coins.
# The seller gives NO change. Find:
#   1. The minimum amount you must pay (≥ P).
#   2. The minimum number of bills/coins to pay that amount.
# The total value of your bills is guaranteed ≥ P.
#
# Input:
#   - Line 1: number of test cases
#   - Each test case:
#       - Line 1: P (price, up to 10000)
#       - Line 2: n (number of bills, up to 100)
#       - Next n lines: value of each bill (up to 10000 each)
#
# Output:
#   For each test case: "amount_paid num_bills"
#
# Approach:
#   0/1 knapsack: dp[s] = min bills to make exactly sum s.
#   Search range [P, P + max_coin] to find the first achievable sum.
# ============================================================

def solve():
    t = int(input())
    for _ in range(t):
        price = int(input())
        n = int(input())
        coins = [int(input()) for _ in range(n)]

        limit = price + max(coins)
        INF = n + 1

        dp = [INF] * (limit + 1)
        dp[0] = 0

        for coin in coins:
            for s in range(limit, coin - 1, -1):
                if dp[s - coin] < INF:
                    dp[s] = min(dp[s], dp[s - coin] + 1)

        for s in range(price, limit + 1):
            if dp[s] < INF:
                print(s, dp[s])
                break


if __name__ == "__main__":
    solve()
