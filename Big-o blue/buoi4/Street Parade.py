# ============================================================
# Problem: Street Parade  (buoi4)
# Source: UVA
# ============================================================
# n floats are stored in a sidestreet. They need to exit onto the
# main street in order 1, 2, 3, ..., n using a stack (LIFO).
# Floats can either go directly to the main street or wait in the stack.
# Determine if it's possible to get them out in order.
#
# Input:
#   - Multiple test cases until n = 0.
#   - Each test case:
#       - Line 1: n
#       - Line 2: n integers (arrival order on main street from sidestreet)
#
# Output:
#   "yes" or "no" for each test case.
#
# Approach:
#   Simulate with a stack. Try to release floats in order 1..n.
#   If at any point the top of stack is not the next expected float
#   and the incoming float also isn't, output "no".
# ============================================================

def solve():
    while True:
        n = int(input())
        if n == 0:
            break

        a = list(map(int, input().split()))
        stack = []
        expected = 1

        ok = True
        for x in a:
            while stack and stack[-1] == expected:
                stack.pop()
                expected += 1
            if x == expected:
                expected += 1
            else:
                stack.append(x)

        while stack:
            if stack[-1] == expected:
                stack.pop()
                expected += 1
            else:
                ok = False
                break

        print("yes" if ok else "no")


if __name__ == "__main__":
    solve()
