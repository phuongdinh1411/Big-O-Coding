# ============================================================
# Problem: Course Schedule
# Source: Big-O
# ============================================================
# There are N courses labeled 0 to N-1. Some courses have prerequisites:
# a pair [u, v] means you must complete course v before course u.
# Determine whether it is possible to finish all N courses.
#
# Input:
#   - Line 1: N M  (courses and number of prerequisite pairs)
#   - Next M lines: u v  (u depends on v)
#
# Output:
#   Print "yes" if all courses can be finished, otherwise "no".
#
# Approach:
#   Cycle detection in a directed graph (DAG check).
#   Use Kahn's BFS algorithm: if fewer than N nodes are processed
#   there is a cycle → impossible.
# ============================================================

from collections import deque, defaultdict


def solve():
    n, m = map(int, input().split())

    graph = defaultdict(list)
    in_degree = [0] * n

    for _ in range(m):
        u, v = map(int, input().split())
        graph[v].append(u)
        in_degree[u] += 1

    queue = deque(i for i in range(n) if in_degree[i] == 0)
    processed = 0

    while queue:
        node = queue.popleft()
        processed += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    print("yes" if processed == n else "no")


if __name__ == "__main__":
    solve()
