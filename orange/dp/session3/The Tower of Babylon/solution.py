# ============================================================
# Problem: The Tower of Babylon
# Source: UVA
# ============================================================
# Given n types of blocks (unlimited supply), each with dimensions x y z.
# A block can be rotated: any two dimensions can serve as the base.
# Stack blocks to build the tallest tower such that each block's base
# is STRICTLY smaller in both dimensions than the block below it.
#
# Input:
#   - Multiple test cases.
#   - Each test case:
#       - Line 1: n (≤ 30)
#       - Next n lines: xi yi zi
#   - Ends with n = 0.
#
# Output:
#   "Case X: maximum height = H"
#
# Approach:
#   Generate all 3 rotations per block, sort by base, then DP:
#   dp[i] = tallest tower with block i on top.
#   dp[i] = blocks[i].height + max(dp[j] for j where base[j] < base[i])
# ============================================================

def solve():
    case = 0
    while True:
        n = int(input())
        if n == 0:
            break
        case += 1

        blocks = []
        for _ in range(n):
            dims = sorted(map(int, input().split()))
            a, b, c = dims
            # 3 orientations: choose each dimension as height
            blocks.append((a, b, c))   # height = largest
            blocks.append((a, c, b))   # height = middle
            blocks.append((b, c, a))   # height = smallest

        blocks.sort()
        m = len(blocks)
        dp = [b[2] for b in blocks]

        for i in range(1, m):
            for j in range(i):
                if blocks[j][0] < blocks[i][0] and blocks[j][1] < blocks[i][1]:
                    dp[i] = max(dp[i], dp[j] + blocks[i][2])

        print(f"Case {case}: maximum height = {max(dp)}")


if __name__ == "__main__":
    solve()
