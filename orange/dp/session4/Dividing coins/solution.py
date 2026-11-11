# ============================================================
# Problem: Dividing Coins
# Source: UVA
# ============================================================
# Divide a bag of m coins between two people as fairly as possible.
# Minimize the absolute difference between the two groups' total values.
#
# Input:
#   - Line 1: n (number of test cases)
#   - Each test case:
#       - Line 1: m (number of coins, m ≤ 100)
#       - Line 2: m coin values (1 to 500 cents each)
#
# Output:
#   For each test case: minimum possible difference.
#
# Approach:
#   Partition problem. Find the largest achievable sum ≤ total/2 using
#   0/1 knapsack DP. Minimum difference = total - 2 * best_sum.
# ============================================================

def solve():
    n = int(input())
    for _ in range(n):
        m = int(input())
        coins = list(map(int, input().split()))

        total = sum(coins)
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for coin in coins:
            for s in range(target, coin - 1, -1):
                if dp[s - coin]:
                    dp[s] = True

        best = max(s for s in range(target + 1) if dp[s])
        print(total - 2 * best)


if __name__ == "__main__":
    solve()
