# ============================================================
# Problem: GukiZ and Contest  (buoi3)
# Source: Codeforces
# ============================================================
# n students participated in a contest. Each student has a score.
# Find the rank of each student: how many students have a STRICTLY
# higher score (rank = 1 + count of students with strictly higher score).
#
# Input:
#   - Line 1: n
#   - Line 2: n integers (scores in original order)
#
# Output:
#   n space-separated ranks (same order as input).
#
# Approach:
#   Sort scores, use binary search (upper_bound) to count students
#   with strictly higher scores. Rank = n - upper_bound_index + 1.
# ============================================================

import bisect


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    sorted_a = sorted(a)

    result = []
    for score in a:
        # Count of scores strictly greater = n - bisect_right(sorted_a, score)
        rank = n - bisect.bisect_right(sorted_a, score) + 1
        result.append(rank)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    solve()
