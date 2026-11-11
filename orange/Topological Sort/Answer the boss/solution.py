# ============================================================
# Problem: Answer the Boss!
# Source: SPOJ
# ============================================================
# In a company with N employees, some employees are "lower" than others
# based on R given relations: "R1 is lower rank than R2".
# Assign each employee a rank (1 = top boss, no one above).
# Employees with the same rank are listed in lexicographical (index) order.
#
# Input:
#   - T test cases.
#   - Each test case:
#       - Line 1: N R
#       - Next R lines: R1 R2  (R1 is lower than R2)
#
# Output:
#   "Scenario #i:" then N lines: "rank employee_index" sorted by rank then index.
#
# Approach:
#   Build directed graph R2 → R1 (boss to subordinate).
#   BFS (Kahn's): rank[v] = max(rank of all predecessors) + 1.
#   Nodes with no incoming edges start at rank 1.
# ============================================================

from collections import defaultdict, deque


def solve():
    t = int(input())

    for case in range(1, t + 1):
        n, r = map(int, input().split())

        adj = defaultdict(list)
        in_degree = [0] * n

        for _ in range(r):
            r1, r2 = map(int, input().split())
            # r1 is lower → r2 is above r1 → edge r2 → r1
            adj[r2].append(r1)
            in_degree[r1] += 1

        rank = [0] * n
        queue = deque()

        for i in range(n):
            if in_degree[i] == 0:
                rank[i] = 1
                queue.append(i)

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                rank[v] = max(rank[v], rank[u] + 1)
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        employees = sorted((rank[i], i) for i in range(n))

        print(f"Scenario #{case}:")
        for rk, idx in employees:
            print(rk, idx)


if __name__ == "__main__":
    solve()
