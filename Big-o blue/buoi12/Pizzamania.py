# ============================================================
# Problem: Pizzamania  (buoi12)
# Source: competitive programming
# ============================================================
# f friends each have some money. A pizza costs p. Find how many
# pairs of friends can together buy exactly one pizza (their combined
# money equals p). Each friend can be in at most one pair.
# Count distinct unordered pairs.
#
# Input:
#   - Line 1: n (test cases)
#   - Each test case:
#       - Line 1: f p
#       - Line 2: f integers (money each friend has)
#
# Output:
#   Number of pairs for each test case.
#
# Approach:
#   Sort the array. For each friend i, binary-search for (p - money[i]).
#   Divide total by 2 (each pair counted twice).
# ============================================================

import bisect


def solve():
    n = int(input())
    for _ in range(n):
        f, p = map(int, input().split())
        money = sorted(map(int, input().split()))

        count = 0
        for i in range(f):
            target = p - money[i]
            if target in money[:i] or target in money[i+1:]:
                # Use binary search
                idx = bisect.bisect_left(money, target)
                if idx < f and money[idx] == target:
                    count += 1

        print(count // 2)


if __name__ == "__main__":
    solve()
