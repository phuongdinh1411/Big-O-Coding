# ============================================================
# Problem: Hierarchy
# Source: SPOJ
# ============================================================
# N students form a company hierarchy. One is the main boss (boss = 0).
# Every other student has exactly one direct boss with a strictly higher salary.
# K successful students (1..K) each specify W students they want to be
# SUPERIOR to (i.e., the boss or boss's boss, etc., of).
#
# Find any valid hierarchy (boss assignment for each student).
#
# Input:
#   - Line 1: N K
#   - Next K lines: W  v1 v2 ... vW
#     (student i+1 wants to be superior to v1..vW, 1-indexed)
#
# Output:
#   N integers: for student i, output 0 if main boss, else direct boss index.
#
# Approach:
#   Build DAG from constraints, DFS topological sort.
#   Chain the topo order: each node's boss = previous node in order.
# ============================================================

from collections import defaultdict
import sys
sys.setrecursionlimit(200000)


def solve():
    n, k = map(int, input().split())

    adj = [[] for _ in range(n)]

    for u in range(k):
        line = list(map(int, input().split()))
        w = line[0]
        for i in range(1, w + 1):
            v = line[i] - 1
            adj[u].append(v)

    visited = [False] * n
    topo = []

    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        topo.append(u)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    topo.reverse()

    boss = [0] * n
    for i in range(1, n):
        boss[topo[i]] = topo[i - 1] + 1  # 1-indexed

    for b in boss:
        print(b)


if __name__ == "__main__":
    solve()
