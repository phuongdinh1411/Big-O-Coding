# ============================================================
# Problem: Monk and his Friends  (buoi13)
# Source: HackerEarth
# ============================================================
# Monk has n packets of candies. Given m queries, each asking whether
# a candy count exists in the current collection:
#   - If found: print "YES".
#   - If NOT found: print "NO" and add it to the collection.
#
# Input:
#   - Line 1: t (test cases)
#   - Each test case:
#       - Line 1: n m
#       - Line 2: n candy counts (initial collection)
#       - Next m lines: one query each
#
# Output:
#   For each query: "YES" or "NO".
# ============================================================

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        candies = set(map(int, input().split()))

        for _ in range(m):
            q = int(input())
            if q in candies:
                print("YES")
            else:
                print("NO")
                candies.add(q)


if __name__ == "__main__":
    solve()
