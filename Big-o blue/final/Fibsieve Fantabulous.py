# ============================================================
# Problem: Fibsieve's Fantabulous  (final)
# Source: UVA / competitive
# ============================================================
# Numbers are arranged in a spiral on a 2D grid. Given a number n,
# find its (row, col) coordinates in the spiral.
# The spiral pattern for a 5×5 grid:
#    1  2  9 10 25
#    4  3  8 11 24
#    5  6  7 12 23
#   16 15 14 13 22
#   17 18 19 20 21
#
# Input:
#   - Line 1: t
#   - Next t lines: a number n
#
# Output:
#   "Case i: col row" for each test case (1-indexed).
#
# Approach:
#   Find which "ring" the number falls in, then determine position.
#   Ring k contains numbers from (2k-3)^2+1 to (2k-1)^2 (for k>=1).
#   Use math to derive row/col.
# ============================================================

import math


def find_pos(n):
    if n == 1:
        return (1, 1)

    # Find the ring (diagonal level)
    k = math.ceil((math.sqrt(n) + 1) / 2)
    side = 2 * k - 1  # the side length of this ring's square

    # Bottom-right corner of ring k is side^2
    br = side * side

    # How far from the BR corner going counterclockwise
    pos_from_br = br - n

    if pos_from_br < side - 1:
        # Bottom row (going left)
        row = side
        col = side - pos_from_br
    elif pos_from_br < 2 * (side - 1):
        # Left column (going up)
        offset = pos_from_br - (side - 1)
        row = side - offset
        col = 1
    elif pos_from_br < 3 * (side - 1):
        # Top row (going right)
        offset = pos_from_br - 2 * (side - 1)
        row = 1
        col = 1 + offset
    else:
        # Right column (going down)
        offset = pos_from_br - 3 * (side - 1)
        row = 1 + offset
        col = side

    return (col, row)


def solve():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        col, row = find_pos(n)
        print(f"Case {i}: {row} {col}")


if __name__ == "__main__":
    solve()
