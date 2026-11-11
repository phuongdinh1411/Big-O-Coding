# ============================================================
# Problem: Pangram  (buoi7)
# Source: HackerRank
# ============================================================
# A pangram is a sentence that contains every letter of the alphabet
# at least once. Given a string of length n, determine if it is a pangram.
#
# Input:
#   - Line 1: n (length of string)
#   - Line 2: the string (may contain upper and lowercase letters)
#
# Output:
#   "YES" if pangram, "NO" otherwise.
#
# Approach:
#   Convert to lowercase and check that all 26 letters are present.
# ============================================================

def solve():
    n = int(input())
    s = input().strip().lower()
    seen = set(s)
    if all(chr(ord('a') + i) in seen for i in range(26)):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
