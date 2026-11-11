# ============================================================
# Problem: Night at the Museum  (buoi1)
# Source: Codeforces
# ============================================================
# A watchman patrols a museum and must check exhibits in a specific
# alphabetical order. The exhibits are arranged in a circle of 26
# positions (a to z). Moving between adjacent positions costs 1 step.
# The watchman can go either direction (shortest path).
# Given the order string, find the total minimum steps to visit all.
#
# Input:
#   - A string of lowercase letters (the visit order).
#
# Output:
#   Total minimum steps.
#
# Approach:
#   For each consecutive pair, cost = min(|diff|, 26 - |diff|).
#   Start at 'a'.
# ============================================================

def solve():
    s = input().strip()
    pos = ord('a')
    total = 0
    for c in s:
        diff = abs(pos - ord(c))
        total += min(diff, 26 - diff)
        pos = ord(c)
    print(total)


if __name__ == "__main__":
    solve()
