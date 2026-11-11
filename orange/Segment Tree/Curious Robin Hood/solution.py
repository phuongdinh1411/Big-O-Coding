# ============================================================
# Problem: Curious Robin Hood
# Source: LightOJ
# ============================================================
# Robin Hood has n sacks (0-indexed), each containing some gold.
# Perform q queries of three types:
#   1 i     → Take all money from sack i (set to 0), print the old value.
#   2 i v   → Add v gold to sack i.
#   3 i j   → Print total gold in sacks i..j (inclusive).
#
# Input:
#   - T test cases.
#   - Each test case:
#       - Line 1: n q
#       - Line 2: n integers (initial gold)
#       - Next q lines: query type and parameters
#
# Output:
#   For each test case print "Case X:" then results of type 1 and 3 queries.
#
# Approach:
#   Fenwick Tree (BIT) for O(log n) point updates and prefix sum queries.
# ============================================================

import sys
input = sys.stdin.readline


def solve():
    t = int(input())

    for case in range(1, t + 1):
        n, q = map(int, input().split())
        arr = list(map(int, input().split()))

        # Fenwick tree (1-indexed)
        bit = [0] * (n + 1)

        def update(i, delta):
            i += 1
            while i <= n:
                bit[i] += delta
                i += i & (-i)

        def prefix(i):
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        def range_sum(l, r):
            return prefix(r) - (prefix(l - 1) if l > 0 else 0)

        for i in range(n):
            update(i, arr[i])

        print(f"Case {case}:")

        for _ in range(q):
            query = list(map(int, input().split()))
            op = query[0]

            if op == 1:
                i = query[1]
                old = arr[i]
                update(i, -old)
                arr[i] = 0
                print(old)
            elif op == 2:
                i, v = query[1], query[2]
                update(i, v)
                arr[i] += v
            else:
                i, j = query[1], query[2]
                print(range_sum(i, j))


if __name__ == "__main__":
    solve()
