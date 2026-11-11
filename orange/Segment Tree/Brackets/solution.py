# ============================================================
# Problem: Brackets
# Source: SPOJ
# ============================================================
# Given a bracket word (string of '(' and ')'), perform two types
# of operations over exactly 10 test cases:
#   0       → Check: is the current string a valid bracket expression?
#   k > 0   → Replace: flip the bracket at 1-indexed position k
#
# A valid bracket expression has equal '(' and ')', and every prefix
# has at least as many '(' as ')'.
#
# Input:
#   - Exactly 10 test cases.
#   - Each test case:
#       - Line 1: n (length of string)
#       - Line 2: n brackets separated by spaces
#       - Line 3: m (number of operations)
#       - Next m lines: integer k (0 = check, k > 0 = flip position k)
#
# Output:
#   For each test case print "Test i:" followed by YES/NO for each check op.
#
# Approach:
#   Segment tree storing (unmatched_open, unmatched_close) per node.
#   Merge: matched = min(left.open, right.close)
#          result  = (left.open - matched + right.open,
#                     left.close + right.close - matched)
#   Valid iff root == (0, 0).
# ============================================================

import sys
input = sys.stdin.readline


def solve():
    for test in range(1, 11):
        n = int(input())
        brackets = input().split()

        tree = [(0, 0)] * (4 * n)

        def merge(left, right):
            matched = min(left[0], right[1])
            return (left[0] - matched + right[0],
                    left[1] + right[1] - matched)

        def build(node, start, end):
            if start == end:
                tree[node] = (1, 0) if brackets[start] == '(' else (0, 1)
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx):
            if start == end:
                tree[node] = (0, 1) if tree[node] == (1, 0) else (1, 0)
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx)
            else:
                update(2 * node + 1, mid + 1, end, idx)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        if n > 0:
            build(1, 0, n - 1)

        m = int(input())
        print(f"Test {test}:")

        for _ in range(m):
            k = int(input())
            if k == 0:
                print("YES" if n > 0 and tree[1] == (0, 0) else "NO")
            else:
                update(1, 0, n - 1, k - 1)


if __name__ == "__main__":
    solve()
