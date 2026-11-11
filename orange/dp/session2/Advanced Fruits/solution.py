# ============================================================
# Problem: Advanced Fruits
# Source: SPOJ
# ============================================================
# Create a new fruit name that is as short as possible and contains
# both original fruit names as substrings. The new name must be the
# Shortest Common Supersequence (SCS) of the two fruit names.
# Example: "apple" + "pear" → "applear" (contains both).
#
# Input:
#   - Multiple lines until EOF, each with two fruit names.
#
# Output:
#   For each pair, the shortest supersequence.
#
# Approach:
#   SCS = LCS backtracking.
#   Build LCS DP table, then trace back: shared characters appear once,
#   non-shared characters from both strings appear in order.
# ============================================================

import sys


def shortest_supersequence(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            result.append(a[i - 1])
            i -= 1
        else:
            result.append(b[j - 1])
            j -= 1
    while i > 0:
        result.append(a[i - 1])
        i -= 1
    while j > 0:
        result.append(b[j - 1])
        j -= 1

    return ''.join(reversed(result))


def main():
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) >= 2:
            print(shortest_supersequence(parts[0], parts[1]))


if __name__ == "__main__":
    main()
