# ============================================================
# Problem: Soldier and Bananas  (buoi7)
# Source: Codeforces
# ============================================================
# A soldier wants to buy c bananas. The i-th banana costs i*a money
# (1-indexed). He already has b money. If the total cost > b, he needs
# to borrow the difference; otherwise he borrows 0.
#
# Input:
#   - Line 1: a b c  (price multiplier, initial money, number of bananas)
#
# Output:
#   Amount to borrow (max 0, cost - b).
#
# Approach:
#   Total cost = a * (1 + 2 + ... + c) = a * c * (c+1) / 2.
#   Answer = max(0, total_cost - b).
# ============================================================

def solve():
    a, b, c = map(int, input().split())
    total = a * c * (c + 1) // 2
    print(max(0, total - b))


if __name__ == "__main__":
    solve()
