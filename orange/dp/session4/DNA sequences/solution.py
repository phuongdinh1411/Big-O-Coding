# ============================================================
# Problem: DNA Sequences
# Source: SPOJ
# ============================================================
# Find the longest common subsequence of two DNA strings where
# all matching segments have length AT LEAST K.
# (Each contiguous matching block must be ≥ K characters long.)
#
# Input:
#   - Multiple test cases until a line with just "0".
#   - Each test case:
#       - Line 1: K (minimum segment length)
#       - Line 2: string 1
#       - Line 3: string 2
#
# Output:
#   For each test case, the length of the longest valid subsequence (or 0).
#
# Approach:
#   match[i][j] = consecutive match length ending at s1[i-1], s2[j-1].
#   dp[i][j] = best valid LCS length considering s1[:i], s2[:j].
#   When match[i][j] >= K:
#     dp[i][j] = max(dp[i][j], dp[i-K][j-K] + K)
#   When match[i][j] > K (extending an already-valid segment):
#     dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
# ============================================================

def solve():
    while True:
        k = int(input())
        if k == 0:
            break

        s1 = input().strip()
        s2 = input().strip()
        n, m = len(s1), len(s2)

        match = [[0] * (m + 1) for _ in range(n + 1)]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                if s1[i - 1] == s2[j - 1]:
                    match[i][j] = match[i - 1][j - 1] + 1

                    if match[i][j] >= k:
                        dp[i][j] = max(dp[i][j],
                                       dp[i - k][j - k] + k)
                    if match[i][j] > k:
                        dp[i][j] = max(dp[i][j],
                                       dp[i - 1][j - 1] + 1)

        print(dp[n][m])


if __name__ == "__main__":
    solve()
