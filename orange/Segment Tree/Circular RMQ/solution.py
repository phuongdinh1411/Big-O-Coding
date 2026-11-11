# ============================================================
# Problem: Circular RMQ
# Source: Codeforces
# ============================================================
# Given a circular array of n integers, support two operations:
#   inc(lf, rg, v) → Add v to all elements in range [lf, rg] (circular)
#   rmq(lf, rg)    → Return the minimum in range [lf, rg] (circular)
#
# Circular means: if lf > rg the range wraps around as [lf, n-1] ∪ [0, rg].
#
# Input:
#   - Line 1: n (1 ≤ n ≤ 200000)
#   - Line 2: n integers (initial array)
#   - Line 3: m (0 ≤ m ≤ 200000)
#   - Next m lines:
#       "lf rg"     → rmq query  (2 integers)
#       "lf rg v"   → inc update (3 integers)
#
# Output:
#   For each rmq query, print the minimum on its own line.
#
# Approach:
#   Segment tree with lazy propagation (additive tags) for range min queries
#   and range add updates. Circular ranges split into at most 2 linear ranges.
# ============================================================

import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    INF = float('inf')
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = arr[start]
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def push_down(node):
        if lazy[node]:
            for child in (2 * node, 2 * node + 1):
                tree[child] += lazy[node]
                lazy[child] += lazy[node]
            lazy[node] = 0

    def update(node, start, end, l, r, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            tree[node] += val
            lazy[node] += val
            return
        push_down(node)
        mid = (start + end) // 2
        update(2 * node, start, mid, l, r, val)
        update(2 * node + 1, mid + 1, end, l, r, val)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def query(node, start, end, l, r):
        if r < start or end < l:
            return INF
        if l <= start and end <= r:
            return tree[node]
        push_down(node)
        mid = (start + end) // 2
        return min(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r))

    build(1, 0, n - 1)

    out = []
    for _ in range(m):
        line = list(map(int, input().split()))
        if len(line) == 2:
            lf, rg = line
            if lf <= rg:
                out.append(query(1, 0, n - 1, lf, rg))
            else:
                out.append(min(query(1, 0, n - 1, lf, n - 1),
                               query(1, 0, n - 1, 0, rg)))
        else:
            lf, rg, v = line
            if lf <= rg:
                update(1, 0, n - 1, lf, rg, v)
            else:
                update(1, 0, n - 1, lf, n - 1, v)
                update(1, 0, n - 1, 0, rg, v)

    print('\n'.join(map(str, out)))


if __name__ == "__main__":
    solve()
