# ============================================================
# Problem: Pick The Sticks
# Source: UVA
# ============================================================
# Place gold sticks on a container of length L. Sticks fully inside
# use their full length. At most ONE stick may hang off each end
# (using only half its length of container space). Maximize total value.
#
# Input:
#   - T test cases.
#   - Each test case:
#       - Line 1: N L
#       - Next N lines: ai vi (stick length, value)
#   - 1 ≤ N ≤ 500, 1 ≤ L ≤ 1000
#
# Output:
#   "Case #x: y"
#
# Approach:
#   0/1 knapsack with 3 states for hanging count (0/1/2).
#   Multiply all lengths by 2 to handle half-lengths as integers.
#   dp[capacity][hanging] = max value.
#   Fully-inside: costs 2*length units; hanging: costs length units.
# ============================================================

def solve():
    t = int(input())
    for case in range(1, t + 1):
        n, L = map(int, input().split())
        sticks = []
        for _ in range(n):
            a, v = map(int, input().split())
            sticks.append((a, v))

        cap = 2 * L
        NEG = float('-inf')

        # dp[c][e] = max value using c capacity units and e hanging edges
        dp = [[NEG] * 3 for _ in range(cap + 1)]
        dp[0][0] = 0

        for length, value in sticks:
            full = 2 * length
            half = length

            for c in range(cap, -1, -1):
                for e in range(3):
                    if dp[c][e] == NEG:
                        continue
                    # Fully inside
                    nc = c + full
                    if nc <= cap:
                        dp[nc][e] = max(dp[nc][e], dp[c][e] + value)
                    # Hanging over one edge
                    if e < 2:
                        nc = c + half
                        if nc <= cap:
                            dp[nc][e + 1] = max(dp[nc][e + 1], dp[c][e] + value)

        ans = max(dp[c][e]
                  for c in range(cap + 1)
                  for e in range(3)
                  if dp[c][e] != NEG)

        print(f"Case #{case}: {ans}")


if __name__ == "__main__":
    solve()
