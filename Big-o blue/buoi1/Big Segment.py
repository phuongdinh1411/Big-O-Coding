# ============================================================
# Problem: Big Segment  (buoi1)
# Source: Codeforces
# ============================================================
# Given n segments [ai, bi], find the 1-indexed position of the segment
# that has the smallest left endpoint AND the largest right endpoint
# (i.e., the "biggest" segment that contains all others).
# If no such segment exists, print -1.
#
# Input:
#   - Line 1: n
#   - Next n lines: ai bi
#
# Output:
#   1-indexed position of the big segment, or -1.
#
# Approach:
#   The big segment must have left = min(all lefts) and right = max(all rights).
#   Scan for a segment satisfying both.
# ============================================================

def solve():
    n = int(input())
    segments = []
    for _ in range(n):
        a, b = map(int, input().split())
        segments.append((a, b))

    min_a = min(s[0] for s in segments)
    max_b = max(s[1] for s in segments)

    for i, (a, b) in enumerate(segments):
        if a == min_a and b == max_b:
            print(i + 1)
            return

    print(-1)


if __name__ == "__main__":
    solve()
