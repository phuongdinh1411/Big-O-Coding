# ============================================================
# Problem: QHEAP1  (buoi6)
# Source: HackerRank
# ============================================================
# Implement a min-heap supporting:
#   1 v  → Insert value v.
#   2 v  → Delete one occurrence of value v.
#   3    → Print the current minimum.
#
# Input:
#   - Line 1: n (number of queries)
#   - Next n lines: query
#
# Output:
#   For each type-3 query, print the minimum.
#
# Approach:
#   Use a heap with a "deleted" multiset for lazy deletion.
# ============================================================

import heapq
from collections import defaultdict


def solve():
    n = int(input())
    heap = []
    deleted = defaultdict(int)

    for _ in range(n):
        parts = input().split()
        op = int(parts[0])

        if op == 1:
            heapq.heappush(heap, int(parts[1]))
        elif op == 2:
            deleted[int(parts[1])] += 1
        else:
            # Pop until we find a non-deleted element
            while heap and deleted[heap[0]] > 0:
                deleted[heap[0]] -= 1
                heapq.heappop(heap)
            print(heap[0])


if __name__ == "__main__":
    solve()
