# ============================================================
# Problem: Compromise
# Source: UVA
# ============================================================
# Two politicians each submit a proposal as a sequence of words.
# Find and print the Longest Common Subsequence (LCS) of their words.
#
# Input:
#   - Multiple test cases until EOF.
#   - Each test case: two texts of words, separated by '#' lines.
#   - Test cases separated by '#'.
#   - Words are lowercase, < 30 chars; texts < 100 words each.
#
# Output:
#   For each test case, print the LCS words separated by spaces.
#
# Approach:
#   Standard LCS DP on word arrays, then backtrack to reconstruct.
# ============================================================

import sys


def lcs_words(w1, w2):
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if w1[i - 1] == w2[j - 1]:
            result.append(w1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return result[::-1]


def main():
    content = sys.stdin.read()
    parts = content.strip().split('#')

    i = 0
    while i + 1 < len(parts):
        text1 = parts[i].split()
        text2 = parts[i + 1].split()
        if text1 and text2:
            print(' '.join(lcs_words(text1, text2)))
        i += 2


if __name__ == "__main__":
    main()
