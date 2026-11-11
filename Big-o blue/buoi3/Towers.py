# ============================================================
# Problem: Towers  (buoi3)
# Source: Codeforces
# ============================================================
# n blocks are available. Build towers: each tower can use only
# blocks of the same height. Find:
#   1. The maximum number of blocks in any single tower (max frequency).
#   2. The total number of distinct towers that can be built
#      (count of distinct block heights that appear at least once).
#
# Input:
#   - Line 1: n
#   - Line 2: n integers (block heights, 1 ≤ height ≤ 1000)
#
# Output:
#   "max_blocks distinct_towers"
#
# Approach:
#   Count frequencies, find max frequency and count of non-zero frequencies.
# ============================================================

from collections import Counter


def solve():
    n = int(input())
    blocks = list(map(int, input().split()))

    freq = Counter(blocks)
    max_blocks = max(freq.values())
    distinct = len(freq)

    print(max_blocks, distinct)


if __name__ == "__main__":
    solve()
