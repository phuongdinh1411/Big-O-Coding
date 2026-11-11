# ============================================================
# Problem: Bytelandian Gold Coins
# Source: SPOJ
# ============================================================
# In Byteland, a coin with value n can be exchanged at a bank for
# three coins: n/2, n/3, and n/4 (all floored). You may also sell
# any coin for n American dollars (1:1 rate). You cannot buy coins.
# Starting with one coin of value n, maximize the dollars you get.
#
# Input:
#   - Several lines, each with an integer n (0 ≤ n ≤ 10^9).
#
# Output:
#   For each n, print the maximum dollars.
#
# Approach:
#   Memoized recursion:
#   f(n) = max(n, f(n//2) + f(n//3) + f(n//4))
#   Use a dict for sparse memoization (n can be up to 10^9).
# ============================================================

import sys
sys.setrecursionlimit(100000)

memo = {}


def solve(n):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    result = max(n, solve(n // 2) + solve(n // 3) + solve(n // 4))
    memo[n] = result
    return result


def main():
    try:
        while True:
            n = int(input())
            print(solve(n))
    except EOFError:
        pass


if __name__ == "__main__":
    main()
