# ============================================================
# Problem: Monk and Multiplication  (buoi6)
# Source: HackerEarth
# ============================================================
# Given n integers added one by one, after each insertion (starting
# from the 3rd), output the product of the 3 smallest numbers seen so far.
# For the first two insertions, output -1.
#
# Input:
#   - Line 1: n
#   - Next n lines: one integer each.
#
# Output:
#   n lines: -1 for first two, then product of 3 smallest for each subsequent.
#
# Approach:
#   Maintain a min-heap of size 3 (or track the 3 smallest incrementally).
# ============================================================

import heapq


def solve():
    n = int(input())
    heap = []

    for i in range(n):
        x = int(input())
        heapq.heappush(heap, x)

        if i < 2:
            print(-1)
        else:
            # Product of 3 smallest
            three = heapq.nsmallest(3, heap)
            print(three[0] * three[1] * three[2])


if __name__ == "__main__":
    solve()
