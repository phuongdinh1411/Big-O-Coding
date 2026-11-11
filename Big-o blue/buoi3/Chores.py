# ============================================================
# Problem: Chores  (buoi3)
# Source: Codeforces
# ============================================================
# There are n chores, each with a difficulty rating. The first a chores
# must be done by one person and the last b chores by another.
# (a + b = n, the assignments don't overlap.)
# The difficulty assigned to the first person is the hardest of their
# chores (max of first a), and the second person's is the max of their b.
# Minimize the difference: max(second group) - max(first group).
#
# Input:
#   - Line 1: n a b
#   - Line 2: n integers (difficulties)
#
# Output:
#   Minimum difference between the two groups' maximums.
#
# Approach:
#   After sorting, one person takes the first a chores, the other takes
#   the last b chores. The split point is between index a-1 and a (0-indexed),
#   so the answer is sorted[a] - sorted[a-1].
# ============================================================

def solve():
    n, a, b = map(int, input().split())
    difficulties = list(map(int, input().split()))
    difficulties.sort()
    # First a chores: max = difficulties[a-1]
    # Last b chores:  max = difficulties[n-1] = difficulties[a+b-1]
    # But we can choose the split: the optimal is at index a and a-1
    print(difficulties[a] - difficulties[a - 1])


if __name__ == "__main__":
    solve()
