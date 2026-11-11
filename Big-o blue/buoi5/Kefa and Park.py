# ============================================================
# Problem: Kefa and Park  (buoi5)
# Source: Codeforces
# ============================================================
# A city is a tree of m nodes. Node 1 is Kefa's home. Each node has a
# cat (1) or no cat (0). Kefa is afraid of seeing more than n cats
# consecutively on any path. A restaurant is a leaf node (degree 1,
# not root). Count how many restaurants Kefa can reach without seeing
# more than n consecutive cats on the path from node 1.
#
# Input:
#   - Line 1: m n
#   - Line 2: m integers (cat[i] for each node)
#   - Next m-1 lines: edges
#
# Output:
#   Number of reachable restaurants.
#
# Approach:
#   BFS from node 1. Track consecutive cats on current path.
#   If consecutive cats exceed n, don't expand. Leaf nodes = restaurants.
# ============================================================

from collections import deque


def solve():
    m, n = map(int, input().split())
    cats = [0] + list(map(int, input().split()))  # 1-indexed

    adj = [[] for _ in range(m + 1)]
    for _ in range(m - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    ans = 0
    # BFS: state = (node, consecutive_cats_ending_here, parent)
    queue = deque([(1, cats[1], 0)])
    visited = [False] * (m + 1)
    visited[1] = True

    while queue:
        node, consec, parent = queue.popleft()

        if consec > n:
            continue

        # Check if leaf (degree 1, not root)
        neighbors = [v for v in adj[node] if v != parent]
        if not neighbors and node != 1:
            ans += 1
            continue

        for v in neighbors:
            if not visited[v]:
                visited[v] = True
                new_consec = consec + cats[v] if cats[v] == 1 else 0
                if cats[v] == 1:
                    new_consec = consec + 1
                else:
                    new_consec = 0
                queue.append((v, new_consec, node))

    print(ans)


if __name__ == "__main__":
    solve()
