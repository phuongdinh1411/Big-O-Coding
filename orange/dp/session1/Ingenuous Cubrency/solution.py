# ============================================================
# Problem: Ingenuous Cubrency
# Source: UVA
# ============================================================
# In Cubeland the currency denominations are all perfect cubes up to 9261:
# 1, 8, 27, 64, ..., 9261  (i.e. 1^3, 2^3, ..., 21^3).
# Count the number of ways to pay a given amount using these coins
# (each coin may be used any number of times).
# Example: 21 cubes → 3 ways:
#   twenty-one 1s  |  one 8 + thirteen 1s  |  two 8s + five 1s
#
# Input:
#   - Lines each containing a positive integer (< 10000).
#
# Output:
#   For each amount, print the number of ways.
#
# Approach:
#   Classic unbounded knapsack / coin-change counting.
#   Precompute dp[0..9999] for all amounts, outer loop = coins.
# ============================================================

import sys

MAX = 10000
coins = [i ** 3 for i in range(1, 22)]  # 1 to 9261

dp = [0] * MAX
dp[0] = 1

for coin in coins:
    for amount in range(coin, MAX):
        dp[amount] += dp[amount - coin]


def main():
    for line in sys.stdin:
        line = line.strip()
        if line:
            print(dp[int(line)])


if __name__ == "__main__":
    main()
