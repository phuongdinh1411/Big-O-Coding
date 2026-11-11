# ============================================================
# Problem: Xenia and Bit Operations
# Source: Codeforces
# ============================================================
# Xenia has a sequence of 2^n non-negative integers.
# She computes value v by:
#   Level 1 (bottom): OR of adjacent pairs  → 2^(n-1) elements
#   Level 2:          XOR of adjacent pairs → 2^(n-2) elements
#   ... alternating until 1 element remains.
#
# Given m queries each setting a[p] = b (1-indexed), print v after each query.
#
# Input:
#   - Line 1: n m  (1 ≤ n ≤ 17, 1 ≤ m ≤ 10^5)
#   - Line 2: 2^n integers
#   - Next m lines: p b
#
# Output:
#   For each query print the resulting value v.
#
# Approach:
#   Perfect segment tree of size 2^n. Leaves store values.
#   Internal node at depth d from leaves uses OR if d is odd, XOR if even.
#   Update propagates O(n) levels up.
# ============================================================

import sys
input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    size = 1 << n

    arr = list(map(int, input().split()))

    tree = [0] * (2 * size)

    # Fill leaves
    for i in range(size):
        tree[size + i] = arr[i]

    # Build internal nodes bottom-up.
    # Node i is at level (n - bit_length(i) + 1) from leaves.
    for i in range(size - 1, 0, -1):
        level = n - (i.bit_length() - 1)
        if level % 2 == 1:
            tree[i] = tree[2 * i] | tree[2 * i + 1]
        else:
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]

    def update(pos, val):
        pos += size
        tree[pos] = val
        level = 1
        pos >>= 1
        while pos >= 1:
            if level % 2 == 1:
                tree[pos] = tree[2 * pos] | tree[2 * pos + 1]
            else:
                tree[pos] = tree[2 * pos] ^ tree[2 * pos + 1]
            pos >>= 1
            level += 1

    out = []
    for _ in range(m):
        p, b = map(int, input().split())
        update(p - 1, b)
        out.append(tree[1])

    sys.stdout.write('\n'.join(map(str, out)) + '\n')


if __name__ == "__main__":
    solve()
