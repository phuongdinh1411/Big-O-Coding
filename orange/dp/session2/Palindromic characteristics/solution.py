# ============================================================
# Problem: Palindromic Characteristics
# Source: Codeforces
# ============================================================
# A 1-palindrome is a string that reads the same forward and backward.
# A k-palindrome (k>1) has its left half equal to its right half,
# AND both halves are (k-1)-palindromes.
#
# The palindromic characteristics of string s is a sequence of |s|
# integers where the i-th number is the count of non-empty substrings
# that are i-palindromes.
#
# Input:
#   - Single string s (1 ≤ |s| ≤ 5000, lowercase).
#
# Output:
#   |s| space-separated integers (counts for k=1 to k=|s|).
#
# Approach:
#   1. Build is_pal[i][j] with standard DP.
#   2. k_level[i][j] = 1 + k_level[i][i + len//2 - 1] if is_pal and len>1.
#   3. Count occurrences per level, then propagate downward
#      (a k-palindrome is also a (k-1)-palindrome).
# ============================================================

def solve():
    s = input().strip()
    n = len(s)

    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for i in range(n - 1):
        is_pal[i][i + 1] = (s[i] == s[i + 1])
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            is_pal[i][j] = (s[i] == s[j]) and is_pal[i + 1][j - 1]

    k_level = [[0] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if is_pal[i][j]:
                if length == 1:
                    k_level[i][j] = 1
                else:
                    half = length // 2
                    k_level[i][j] = 1 + k_level[i][i + half - 1]

    count = [0] * (n + 2)
    for i in range(n):
        for j in range(i, n):
            if is_pal[i][j]:
                count[k_level[i][j]] += 1

    # Propagate: a k-palindrome is also (k-1)-palindrome
    for k in range(n, 0, -1):
        count[k - 1] += count[k]

    print(' '.join(map(str, count[1:n + 1])))


if __name__ == "__main__":
    solve()
