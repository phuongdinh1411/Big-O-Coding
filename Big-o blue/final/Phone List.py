# ============================================================
# Problem: Phone List  (final)
# Source: Kattis / UVA
# ============================================================
# Given a list of phone numbers, determine if it is "consistent":
# no phone number is a prefix of another. If any number is a prefix
# of another, print "NO"; otherwise print "YES".
#
# Input:
#   - Line 1: t (test cases)
#   - Each test case:
#       - Line 1: n
#       - Next n lines: a phone number (string of digits)
#
# Output:
#   "YES" or "NO" for each test case.
#
# Approach:
#   Sort numbers. If any number is a prefix of the next one, print "NO".
#   (A prefix can only be adjacent after sorting.)
# ============================================================

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = [input().strip() for _ in range(n)]
        numbers.sort()

        consistent = True
        for i in range(n - 1):
            if numbers[i + 1].startswith(numbers[i]):
                consistent = False
                break

        print("YES" if consistent else "NO")


if __name__ == "__main__":
    solve()
