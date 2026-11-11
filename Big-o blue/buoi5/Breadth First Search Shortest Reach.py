# ============================================================
# Problem: Breadth First Search: Shortest Reach  (buoi5)
# Source: HackerRank
# ============================================================
# Given an undirected graph with n nodes and m edges (each edge weight 6),
# and a source node s, find the shortest distance from s to every other node.
# Print -1 for unreachable nodes. Do NOT print distance to s itself.
#
# Input:
#   - q queries.
#   - Each query:
#       - Line 1: n m (nodes and edges)
#       - Next m lines: a b (edge)
#       - Last line: s (source, 1-indexed)
#
# Output:
#   For each query, distances to nodes 1..n (excluding s), space-separated.
#
# Approach:
#   BFS. Each edge has weight 6, so BFS distance * 6 = shortest path.
# ============================================================

from collections import deque


def solve():
    q = int(input())
    for _ in range(q):
        n, m = map(int, input().split())
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)
        s = int(input())

        dist = [-1] * (n + 1)
        dist[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 6
                    queue.append(v)

        result = [dist[i] for i in range(1, n + 1) if i != s]
        print(' '.join(map(str, result)))


if __name__ == "__main__":
    solve()
