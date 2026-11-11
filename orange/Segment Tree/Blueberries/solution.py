# ============================================================
# Problem: Blueberries
# Source: SPOJ
# ============================================================
# Teresa wants to pick blueberries from N bushes arranged in a row.
# If she picks from bush i, she CANNOT pick from the adjacent bush i+1.
# She will pick at most K blueberries from any single bush.
# Find the maximum total blueberries she can collect.
#
# Input:
#   - First line: T (number of test cases)
#   - Each test case:
#       - First line: N (number of bushes) and K (max per bush)
#       - Second line: N integers (blueberries in each bush)
#
# Output:
#   For each test case: "Scenario #i: X" where X is the maximum.
#
# Constraints:
#   1 ≤ N ≤ 1000, 1 ≤ K ≤ 1000
#
# Approach:
#   Classic "House Robber" DP. Cap each bush at K, then:
#   dp[i] = max(dp[i-1], dp[i-2] + berries[i])
# ============================================================

def solve():
    t = int(input())

    for case in range(1, t + 1):
        n, k = map(int, input().split())
        berries = list(map(int, input().split()))

        # Cap each bush at K
        berries = [min(b, k) for b in berries]

        if n == 0:
            print(f"Scenario #{case}: 0")
            continue
        if n == 1:
            print(f"Scenario #{case}: {berries[0]}")
            continue

        prev2 = berries[0]
        prev1 = max(berries[0], berries[1])

        for i in range(2, n):
            curr = max(prev1, prev2 + berries[i])
            prev2 = prev1
            prev1 = curr

        print(f"Scenario #{case}: {prev1}")


if __name__ == "__main__":
    solve()
