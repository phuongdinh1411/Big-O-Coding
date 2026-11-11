# ============================================================
# Problem: Pasha and Tea  (buoi3)
# Source: Codeforces
# ============================================================
# n boys and n girls will drink tea. There are 2n cups of tea with
# varying amounts. Boys get the larger amounts, girls the smaller.
# Each boy must get the same amount (limited by the smallest boy cup).
# Each girl must get the same amount (limited by the smallest girl cup
# and half the smallest boy amount). Also limited by total tea q.
# Find the maximum total tea consumed (3 * amount_per_person * n).
#
# Input:
#   - Line 1: n q  (n boys + n girls, total tea q)
#   - Line 2: 2n integers (cup sizes)
#
# Output:
#   Maximum total tea (one decimal place).
#
# Approach:
#   Sort all 2n values. Girls get the n smallest, boys the n largest.
#   Max per girl = min(smallest_girl_cup, smallest_boy_cup / 2).
#   Also limited by q / (3n) (equal share of budget).
#   Answer = 3 * min(per_girl_max) * n.
# ============================================================

def solve():
    n, q = map(int, input().split())
    cups = sorted(map(int, input().split()))

    girl_min = cups[0]      # smallest girl's cup
    boy_min = cups[n]       # smallest boy's cup

    per_person = min(float(girl_min), float(boy_min) / 2, float(q) / (3 * n))
    print(f"{3 * per_person * n:.1f}")


if __name__ == "__main__":
    solve()
