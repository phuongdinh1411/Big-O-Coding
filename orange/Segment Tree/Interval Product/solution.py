# ============================================================
# Problem: Interval Product
# Source: UVALive
# ============================================================
# Given a sequence of N integers, perform K operations:
#   C i v  → Set the i-th element (1-indexed) to v.
#   P i j  → Output the sign of the product Xi * Xi+1 * ... * Xj.
#             '+' if positive, '-' if negative, '0' if zero.
#
# Input:
#   - Multiple test cases until EOF.
#   - Each test case:
#       - Line 1: N K
#       - Line 2: N integers (-100 to 100)
#       - Next K lines: "C i v" or "P i j"
#
# Output:
#   For each test case print a string of signs ('+', '-', '0') for all P ops.
#
# Approach:
#   Segment tree storing the sign (-1, 0, +1) of each element.
#   The sign of a product is the product of individual signs.
#   merge(l, r) = l * r  (sign multiplication is exact in {-1,0,1}).
# ============================================================

import sys
input = sys.stdin.readline


def solve():
    while True:
        line = input().split()
        if not line:
            break

        n, k = int(line[0]), int(line[1])
        arr = list(map(int, input().split()))

        tree = [1] * (4 * n)

        def sign(v):
            return 0 if v == 0 else (1 if v > 0 else -1)

        def build(node, start, end):
            if start == end:
                tree[node] = sign(arr[start])
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = tree[2 * node] * tree[2 * node + 1]

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = sign(val)
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = tree[2 * node] * tree[2 * node + 1]

        def query(node, start, end, l, r):
            if r < start or end < l:
                return 1   # identity for multiplication
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            return (query(2 * node, start, mid, l, r) *
                    query(2 * node + 1, mid + 1, end, l, r))

        build(1, 0, n - 1)

        result = []
        for _ in range(k):
            parts = input().split()
            op = parts[0]
            if op == 'C':
                i, v = int(parts[1]) - 1, int(parts[2])
                update(1, 0, n - 1, i, v)
            else:
                i, j = int(parts[1]) - 1, int(parts[2]) - 1
                s = query(1, 0, n - 1, i, j)
                result.append('0' if s == 0 else ('-' if s < 0 else '+'))

        print(''.join(result))


if __name__ == "__main__":
    solve()
