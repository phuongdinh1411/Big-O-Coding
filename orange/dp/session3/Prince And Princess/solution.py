# ============================================================
# Problem: Prince And Princess
# Source: UVA
# ============================================================
# On an n×n chessboard (cells numbered 1..n²), Prince visits p+1 cells
# and Princess visits q+1 cells. Each sequence contains distinct values.
# Find the length of their Longest Common Subsequence (LCS).
#
# Input:
#   - Multiple test cases.
#   - Each test case:
#       - Line 1: n p q
#       - Line 2: p+1 integers (Prince's path)
#       - Line 3: q+1 integers (Princess's path)
#
# Output:
#   "Case X: L" where L is the LCS length.
#
# Approach:
#   LCS of two sequences with distinct elements = LIS after index mapping.
#   Map Prince's sequence elements to positions 0..p.
#   Replace Princess's sequence with those positions (skip missing).
#   LCS length = LIS length of the transformed sequence.
#   O((p+q) log p) instead of O(p*q).
# ============================================================

import bisect
import sys
input = sys.stdin.readline


def solve():
    case = 0
    while True:
        line = input()
        if not line:
            break
        line = line.split()
        if not line:
            break
        n, p, q = int(line[0]), int(line[1]), int(line[2])
        case += 1

        prince = list(map(int, input().split()))
        princess = list(map(int, input().split()))

        pos = {v: i for i, v in enumerate(prince)}
        seq = [pos[v] for v in princess if v in pos]

        tails = []
        for x in seq:
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x

        print(f"Case {case}: {len(tails)}")


if __name__ == "__main__":
    solve()
