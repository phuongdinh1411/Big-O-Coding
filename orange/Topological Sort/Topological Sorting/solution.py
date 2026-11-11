# ============================================================
# Problem: Topological Sorting
# Source: SPOJ
# ============================================================
# Sandro has n tasks (1..n) and m dependencies: "x must be done before y".
# Find an ordering of all tasks respecting all dependencies.
# If impossible (cycle exists), print "Sandro fails."
# Among all valid orderings, print the lexicographically smallest one.
#
# Input:
#   - Line 1: n m  (1 ≤ n ≤ 10000, 1 ≤ m ≤ 1000000)
#   - Next m lines: x y  (task x before task y)
#
# Output:
#   Space-separated ordering, or "Sandro fails."
#
# Approach:
#   Kahn's algorithm with a min-heap to always pick the smallest
#   available task → guarantees lexicographically smallest result.
# ============================================================

import heapq
from collections import defaultdict


def solve():
    n, m = map(int, input().split())

    adj = defaultdict(list)
    in_degree = [0] * (n + 1)

    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        in_degree[y] += 1

    heap = [i for i in range(1, n + 1) if in_degree[i] == 0]
    heapq.heapify(heap)

    result = []
    while heap:
        u = heapq.heappop(heap)
        result.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)

    if len(result) < n:
        print("Sandro fails.")
    else:
        print(' '.join(map(str, result)))


if __name__ == "__main__":
    solve()
