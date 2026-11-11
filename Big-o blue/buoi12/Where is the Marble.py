# ============================================================
# Problem: Where is the Marble?  (buoi12)
# Source: UVA
# ============================================================
# Given n marbles with numbers and q queries, for each query find the
# 1-indexed position of a marble with that number (after sorting).
# If not found, print "X not found".
#
# Input:
#   - Multiple test cases until "0 0".
#   - Each test case:
#       - Line 1: n q
#       - Line 2: n marble numbers
#       - Line 3: q query numbers
#
# Output:
#   "CASE# X:\n" then results for each query.
#
# Approach:
#   Sort marbles, binary search for each query.
# ============================================================

import bisect


def solve():
    case = 1
    while True:
        n, q = map(int, input().split())
        if n == 0 and q == 0:
            break

        marbles = sorted(map(int, input().split()))
        queries = list(map(int, input().split()))

        print(f"CASE# {case}:")
        case += 1

        for qval in queries:
            idx = bisect.bisect_left(marbles, qval)
            if idx < n and marbles[idx] == qval:
                print(f"{qval} found at {idx + 1}")
            else:
                print(f"{qval} not found")


if __name__ == "__main__":
    solve()
