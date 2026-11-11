# ============================================================
# Problem: LCS of Three Strings
# Source: GeeksforGeeks
# ============================================================
# Given three strings X, Y, Z, find the length of their
# Longest Common Subsequence (LCS).
#
# Input:
#   - T test cases.
#   - Each test case:
#       - Line 1: n m k  (lengths of X, Y, Z)
#       - Line 2: X Y Z (space-separated)
#   - 1 ≤ T ≤ 100, 1 ≤ N,M,K ≤ 100
#
# Output:
#   For each test case, print the LCS length.
#
# Approach:
#   3D DP: dp[i][j][l] = LCS of X[:i], Y[:j], Z[:l].
#   If X[i-1]==Y[j-1]==Z[l-1]: dp[i][j][l] = dp[i-1][j-1][l-1] + 1
#   else: dp[i][j][l] = max(dp[i-1][j][l], dp[i][j-1][l], dp[i][j][l-1])
# ============================================================

def solve():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        X, Y, Z = input().split()

        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for l in range(1, k + 1):
                    if X[i - 1] == Y[j - 1] == Z[l - 1]:
                        dp[i][j][l] = dp[i - 1][j - 1][l - 1] + 1
                    else:
                        dp[i][j][l] = max(dp[i - 1][j][l],
                                          dp[i][j - 1][l],
                                          dp[i][j][l - 1])

        print(dp[n][m][k])


if __name__ == "__main__":
    solve()
