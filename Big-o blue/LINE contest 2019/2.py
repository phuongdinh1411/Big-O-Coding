# ============================================================
# Problem: LINE Contest 2019 - Problem 2  (Message Fix)
# Source: LINE Contest 2019
# ============================================================
# Given a dictionary of n correct messages and m queries (possibly
# corrupted messages), for each query determine if it can be "fixed"
# to match any dictionary message by changing at most ONE character.
# Print "CAN FIX" or "CAN NOT FIX" for each query.
#
# Note: Two strings match if they have the same length and differ in
# at most one position.
#
# Input:
#   - Line 1: n m
#   - Next n lines: dictionary messages
#   - Next m lines: query messages
#
# Output:
#   "CAN FIX" or "CAN NOT FIX" for each query (case-insensitive compare).
# ============================================================

def is_match(a, b):
    if len(a) != len(b):
        return False
    diff = sum(1 for x, y in zip(a.lower(), b.lower()) if x != y)
    return diff <= 1


def solve():
    n, m = map(int, input().split())
    messages = [input().strip() for _ in range(n)]

    for _ in range(m):
        query = input().strip()
        if any(is_match(query, msg) for msg in messages):
            print("CAN FIX")
        else:
            print("CAN NOT FIX")


if __name__ == "__main__":
    solve()
