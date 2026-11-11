# ============================================================
# Problem: Testing the CATCHER
# Source: UVA
# ============================================================
# A CATCHER missile defense system intercepts missiles in sequence.
# It can intercept missile i if:
#   - It's the first missile to intercept, OR
#   - The missile's height ≤ the last intercepted missile's height.
# Find the maximum number of missiles that can be intercepted
# (Longest Non-Increasing Subsequence).
#
# Input:
#   - Multiple test cases; each is a sequence of heights ending with -1.
#   - Input ends when the first value is -1.
#
# Output:
#   For each test case (blank line between cases):
#     "Test #X:"
#     "  maximum possible number of missiles intercepted: Y"
#
# Approach:
#   Longest Non-Increasing Subsequence = LIS on negated values
#   (using bisect_right to allow equal elements).
# ============================================================

import bisect
import sys


def longest_non_increasing(arr):
    tails = []
    for x in arr:
        neg = -x
        idx = bisect.bisect_right(tails, neg)
        if idx == len(tails):
            tails.append(neg)
        else:
            tails[idx] = neg
    return len(tails)


def main():
    data = sys.stdin.read().split()
    idx = 0
    case = 0

    while idx < len(data):
        missiles = []
        while idx < len(data):
            h = int(data[idx])
            idx += 1
            if h == -1:
                break
            missiles.append(h)

        if not missiles:
            break

        case += 1
        result = longest_non_increasing(missiles)

        if case > 1:
            print()
        print(f"Test #{case}:")
        print(f"  maximum possible number of missiles intercepted: {result}")


if __name__ == "__main__":
    main()
