# ============================================================
# Problem: Distinct Count  (buoi13)
# Source: HackerEarth
# ============================================================
# Given t test cases, each with an array of n integers and a number x,
# classify the array:
#   - "Bad"     if distinct count < x
#   - "Good"    if distinct count == x
#   - "Average" if distinct count > x
#
# Input:
#   - Line 1: t
#   - Each test case:
#       - Line 1: n x
#       - Line 2: n integers
#
# Output:
#   "Bad", "Good", or "Average" for each test case.
# ============================================================

def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        distinct = len(set(a))
        if distinct < x:
            print("Bad")
        elif distinct == x:
            print("Good")
        else:
            print("Average")


if __name__ == "__main__":
    solve()
