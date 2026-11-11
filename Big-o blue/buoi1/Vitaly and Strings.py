# ============================================================
# Problem: Vitaly and Strings  (buoi1)
# Source: Codeforces
# ============================================================
# Given two strings s and t of equal length (lowercase), find a string
# r such that s < r < t in lexicographic order, or print "No such string"
# if impossible.
# r must be lexicographically between s and t (strictly).
#
# Input:
#   - Line 1: string s
#   - Line 2: string t
#
# Output:
#   A string r with s < r < t, or "No such string".
#
# Approach:
#   Try to increment s by 1 (like adding 1 to a base-26 number).
#   If the result r < t, output r; otherwise "No such string".
# ============================================================

def solve():
    s = input().strip()
    t = input().strip()
    n = len(s)

    # Increment s by 1 in base-26
    r = list(s)
    carry = 1
    for i in range(n - 1, -1, -1):
        val = ord(r[i]) - ord('a') + carry
        r[i] = chr(ord('a') + val % 26)
        carry = val // 26
        if carry == 0:
            break

    if carry:
        print("No such string")
        return

    r_str = ''.join(r)
    if r_str < t:
        print(r_str)
    else:
        print("No such string")


if __name__ == "__main__":
    solve()
