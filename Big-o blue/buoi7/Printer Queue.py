# ============================================================
# Problem: Printer Queue  (buoi7)
# Source: UVA
# ============================================================
# A printer queue processes jobs with priorities. The printer always
# prints the job with the highest priority first. If the front job is
# not the highest priority, it moves to the back. Find how many pages
# are printed before a specific job (at position b, 0-indexed) is printed.
#
# Input:
#   - Line 1: n (test cases)
#   - Each test case:
#       - Line 1: a b  (a jobs, target at position b)
#       - Line 2: a priority values
#
# Output:
#   For each test case: the 1-indexed position at which the target job is printed.
#
# Approach:
#   Simulate with a queue and a max-heap. Always print the max-priority job.
# ============================================================

from collections import deque
import heapq


def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        priorities = list(map(int, input().split()))

        queue = deque((p, i) for i, p in enumerate(priorities))
        max_heap = [-p for p in priorities]
        heapq.heapify(max_heap)

        order = 0
        while queue:
            p, idx = queue[0]
            if p == -max_heap[0]:
                queue.popleft()
                heapq.heappop(max_heap)
                order += 1
                if idx == b:
                    print(order)
                    break
            else:
                queue.rotate(-1)


if __name__ == "__main__":
    solve()
