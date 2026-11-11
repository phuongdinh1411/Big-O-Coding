# ============================================================
# Problem: Add All  (buoi6)
# Source: UVA
# ============================================================
# Given n numbers, repeatedly add the two smallest numbers. The cost
# of each addition is the sum of the two numbers. Find the minimum
# total cost to add all numbers into one.
# (This is the Huffman coding / greedy problem.)
#
# Input:
#   - Multiple test cases until n = 0.
#   - Each test case: n on one line, then n integers.
#
# Output:
#   Minimum total cost for each test case.
#
# Approach:
#   Min-heap: always merge the two smallest. Total cost = sum of all merges.
# ============================================================

import heapq


def solve():
    while True:
        n = int(input())
        if n == 0:
            break

        nums = list(map(int, input().split()))
        heapq.heapify(nums)

        total_cost = 0
        while len(nums) > 1:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            total_cost += a + b
            heapq.heappush(nums, a + b)

        print(total_cost)


if __name__ == "__main__":
    solve()
