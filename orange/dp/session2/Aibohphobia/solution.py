# ============================================================
# Problem: Aibohphobia
# Source: SPOJ
# ============================================================
# Given a string S, find the minimum number of characters to INSERT
# to make it a palindrome.
# Example: "fft" → "tfft" (insert 1 char).
#
# Input:
#   - Multiple test cases, one string per line (max 6100 chars).
#
# Output:
#   For each string, print the minimum insertions needed.
#
# Approach:
#   Minimum insertions = len(S) - LPS(S)
#   where LPS (Longest Palindromic Subsequence) = LCS(S, reverse(S)).
#   Use space-optimized LCS with two rows.
# ============================================================

import sys


def solve():
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue

        n = len(s)
        rev = s[::-1]

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev, curr = curr, [0] * (n + 1)

        lps = prev[n]
        print(n - lps)


if __name__ == "__main__":
    solve()
