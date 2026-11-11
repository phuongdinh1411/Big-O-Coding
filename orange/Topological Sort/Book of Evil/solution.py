# ============================================================
# Problem: Book of Evil
# Source: Codeforces
# ============================================================
# n settlements connected as a tree (n-1 bidirectional paths).
# The "Book of Evil" has damage range d: it affects all settlements
# within distance d. You are told m settlements that are definitely
# affected. Find how many settlements could possibly contain the Book.
#
# Input:
#   - Line 1: n m d  (1 ≤ m ≤ n ≤ 100000, 0 ≤ d ≤ n-1)
#   - Line 2: m distinct integers (affected settlements, 1-indexed)
#   - Next n-1 lines: a b  (edge between a and b)
#
# Output:
#   Number of settlements that may contain the Book (0 if none).
#
# Approach:
#   A settlement is valid iff its max distance to any affected node ≤ d.
#   The "farthest" affected node from any settlement is one of the two
#   diameter endpoints of the affected set. Perform 3 BFS to find them.
# ============================================================

from collections import deque


def solve():
    n, m, d = map(int, input().split())
    affected = list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        return dist

    # Diameter endpoints of affected set
    dist1 = bfs(affected[0])
    u = max(affected, key=lambda x: dist1[x])

    dist_u = bfs(u)
    v = max(affected, key=lambda x: dist_u[x])

    dist_v = bfs(v)

    count = sum(1 for i in range(1, n + 1)
                if max(dist_u[i], dist_v[i]) <= d)
    print(count)


if __name__ == "__main__":
    solve()
