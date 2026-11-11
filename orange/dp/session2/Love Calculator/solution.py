# ============================================================
# Problem: Love Calculator
# Source: LightOJ
# ============================================================
# Given two names A and B, find:
#   1. The length of the shortest string that contains both names
#      as subsequences (Shortest Common Supersequence length).
#   2. The number of distinct shortest such strings.
#
# Input:
#   - T test cases (T ≤ 125).
#   - Each test case: two lines with names (≤ 30 capital letters).
#
# Output:
#   "Case X: L C" where L = SCS length, C = count of distinct SCS.
#
# Approach:
#   SCS length = len(A) + len(B) - LCS(A, B).
#   Count via DP: when chars match → cnt[i][j] = cnt[i-1][j-1].
#   When chars differ → add counts from optimal LCS directions.
# ============================================================

def solve():
    t = int(input())

    for case in range(1, t + 1):
        a = input().strip()
        b = input().strip()
        m, n = len(a), len(b)

        lcs = [[0] * (n + 1) for _ in range(m + 1)]
        cnt = [[0] * (n + 1) for _ in range(m + 1)]

        cnt[0][0] = 1
        for i in range(1, m + 1):
            cnt[i][0] = 1
        for j in range(1, n + 1):
            cnt[0][j] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                    cnt[i][j] = cnt[i - 1][j - 1]
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
                    if lcs[i - 1][j] > lcs[i][j - 1]:
                        cnt[i][j] = cnt[i - 1][j]
                    elif lcs[i][j - 1] > lcs[i - 1][j]:
                        cnt[i][j] = cnt[i][j - 1]
                    else:
                        cnt[i][j] = cnt[i - 1][j] + cnt[i][j - 1]

        scs_len = m + n - lcs[m][n]
        print(f"Case {case}: {scs_len} {cnt[m][n]}")


if __name__ == "__main__":
    solve()
