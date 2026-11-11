# ============================================================
# Problem: Beverages
# Source: UVA
# ============================================================
# Dilbert has N beverages. He must drink them in non-decreasing
# alcohol order. Some constraints state "B1 must be drunk before B2".
# When multiple valid choices exist, always pick the one that
# appeared first in the input (smallest input index).
#
# Input:
#   - Multiple test cases until EOF.
#   - Each test case:
#       - Line 1: N (number of beverages)
#       - Next N lines: beverage name
#       - Line: M (number of ordering constraints)
#       - Next M lines: "B1 B2" (B1 before B2)
#       - Blank line after each test case.
#
# Output:
#   "Case #C: Dilbert should drink beverages in this order: B1 B2 ... BN."
#   followed by a blank line.
#
# Approach:
#   Kahn's topological sort with a min-heap to always prefer the
#   beverage with the smallest input index among equal in-degree nodes.
# ============================================================

import heapq
from collections import defaultdict
import sys


def solve():
    case_num = 0

    try:
        while True:
            n = int(input())
            case_num += 1

            beverages = []
            name_to_id = {}
            for i in range(n):
                name = input().strip()
                beverages.append(name)
                name_to_id[name] = i

            graph = defaultdict(list)
            in_degree = [0] * n

            m = int(input())
            for _ in range(m):
                parts = input().split()
                u = name_to_id[parts[0]]
                v = name_to_id[parts[1]]
                graph[u].append(v)
                in_degree[v] += 1

            # skip blank line
            try:
                input()
            except Exception:
                pass

            heap = [i for i in range(n) if in_degree[i] == 0]
            heapq.heapify(heap)

            result = []
            while heap:
                u = heapq.heappop(heap)
                result.append(beverages[u])
                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        heapq.heappush(heap, v)

            print(f"Case #{case_num}: Dilbert should drink beverages in this order: {' '.join(result)}.")
            print()

    except EOFError:
        pass


if __name__ == "__main__":
    solve()
