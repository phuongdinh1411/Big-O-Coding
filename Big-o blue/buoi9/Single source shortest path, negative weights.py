# ============================================================
# Problem: Single Source Shortest Path, Negative Weights  (buoi9)
# Source: Kattis / competitive
# ============================================================
# Given a directed graph with n nodes, m edges (possibly negative weights),
# and q queries, find the shortest path from source s to each queried node.
# If the node is on or reachable from a negative cycle, print "-Infinity".
# If unreachable, print "Impossible".
#
# Input:
#   - Multiple test cases until "0 0 0 0".
#   - Each test case:
#       - Line 1: n m q s  (nodes, edges, queries, source, 0-indexed)
#       - Next m lines: u v w (directed edge)
#       - Next q lines: v (query node)
#
# Output:
#   For each query: distance, "-Infinity", or "Impossible". Blank line between.
#
# Approach:
#   Bellman-Ford. Nodes relaxed in a (n+1)..2n extra iteration pass
#   are on/reachable from negative cycles.
# ============================================================

def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0

    results = []
    first = True

    while idx < len(input_data):
        n, m, q, s = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2]), int(input_data[idx+3])
        idx += 4
        if n == 0:
            break

        edges = []
        for _ in range(m):
            u, v, w = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])
            idx += 3
            edges.append((u, v, w))

        INF = float('inf')
        dist = [INF] * n
        dist[s] = 0

        for _ in range(n - 1):
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        neg_inf = [False] * n
        for _ in range(n):
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    neg_inf[v] = True
                if neg_inf[u]:
                    neg_inf[v] = True

        block = []
        for _ in range(q):
            v = int(input_data[idx]); idx += 1
            if neg_inf[v]:
                block.append("-Infinity")
            elif dist[v] == INF:
                block.append("Impossible")
            else:
                block.append(str(dist[v]))

        if not first:
            results.append("")
        first = False
        results.extend(block)

    print('\n'.join(results))


if __name__ == "__main__":
    solve()
