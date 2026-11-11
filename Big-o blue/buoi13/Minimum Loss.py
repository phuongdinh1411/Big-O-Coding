# ============================================================
# Problem: Minimum Loss  (buoi13)
# Source: Codeforces
# ============================================================
# Lauren has price predictions for a house for n years: p1, p2, ..., pn.
# She buys at year i and sells at year j (i < j). She wants to minimize
# the loss: p[i] - p[j] where p[i] > p[j] (selling lower than buying).
# Find the minimum loss (minimum positive difference where buy > sell).
#
# Input:
#   - Line 1: n
#   - Line 2: n integers (prices, all distinct)
#
# Output:
#   Minimum loss.
#
# Approach:
#   Process prices left to right. Maintain a sorted set of seen prices.
#   For price p[i], find the smallest value in the set greater than p[i]
#   (that's a future sell lower than buy scenario... actually reverse).
#   Actually: we look for the smallest price GREATER than p[i] from 
#   PREVIOUS prices (earlier years) → that was the buy price.
#   min loss = min(prev_buy - p[i]) where prev_buy > p[i].
# ============================================================

import bisect


def solve():
    n = int(input())
    prices = list(map(int, input().split()))

    # For each i, find smallest previous price > prices[i]
    # That gives a buy-then-sell with minimum positive loss
    seen = []
    ans = float('inf')

    for i in range(1, n):
        bisect.insort(seen, prices[i - 1])
        # Find smallest in seen strictly > prices[i]
        idx = bisect.bisect_right(seen, prices[i])
        if idx < len(seen):
            ans = min(ans, seen[idx] - prices[i])

    print(ans)


if __name__ == "__main__":
    solve()
