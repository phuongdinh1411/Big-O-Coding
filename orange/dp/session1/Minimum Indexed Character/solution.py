# ============================================================
# Problem: Minimum Indexed Character
# Source: GeeksforGeeks
# ============================================================
# Given two strings str and patt, find the character in patt that
# appears at the minimum index in str. If no character of patt is
# present in str, print "No character present".
#
# Input:
#   - Line 1: T (test cases)
#   - Each test case: one line with str and patt separated by space.
#   - 1 ≤ T ≤ 10^5
#
# Output:
#   For each test case: the matching character or "No character present".
#
# Approach:
#   Record the first occurrence index of each character in str.
#   Iterate patt characters and return the one with the smallest index in str.
# ============================================================

import sys
input = sys.stdin.readline


def solve():
    t = int(input())
    for _ in range(t):
        s, p = input().split()

        # Map each char to its first index in s
        first = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i

        best_char = None
        best_idx = float('inf')
        for c in p:
            if c in first and first[c] < best_idx:
                best_idx = first[c]
                best_char = c

        print(best_char if best_char is not None else "No character present")


if __name__ == "__main__":
    solve()
