# ============================================================
# Problem: Bear and Game  (buoi1)
# Source: Codeforces
# ============================================================
# Bear Limak watches a football game. The game lasts 90 minutes.
# There are n key moments (minutes) where Limak can do something exciting.
# Between any two consecutive actions, the gap must be ≤ 15 minutes.
# The gap from the last action to minute 90 must also be ≤ 15.
# If any gap exceeds 15, Limak leaves (only earns +15 more minutes).
# Find the total minutes Limak watches.
#
# Input:
#   - Line 1: n (number of key moments)
#   - Line 2: n integers (minutes of key moments, strictly increasing)
#
# Output:
#   Total minutes watched.
#
# Approach:
#   Iterate through moments. If current gap ≤ 15, continue.
#   Otherwise Limak leaves: total = last_time + 15.
#   After all moments, check gap to minute 90.
# ============================================================

def solve():
    n = int(input())
    moments = list(map(int, input().split()))

    last = 0
    for t in moments:
        if t - last <= 15:
            last = t
        else:
            print(last + 15)
            return

    if 90 - last <= 15:
        print(90)
    else:
        print(last + 15)


if __name__ == "__main__":
    solve()
