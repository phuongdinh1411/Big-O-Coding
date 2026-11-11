# ============================================================
# Problem: Transforms the Expression  (buoi4)
# Source: competitive programming
# ============================================================
# Convert an infix expression to postfix (Reverse Polish Notation).
# The expression uses single-character operands and operators +,-,*,/,^,
# with properly balanced parentheses. Each pair of parentheses wraps
# exactly one operator with its two operands.
#
# Input:
#   - Line 1: n (number of expressions)
#   - Next n lines: one infix expression each.
#
# Output:
#   For each expression, the postfix representation.
#
# Approach:
#   Since every operator is between parentheses, use a stack:
#   - Operands: print immediately.
#   - Operators: push to stack.
#   - ')': pop and print the top operator.
#   - '(': ignore.
# ============================================================

def solve():
    n = int(input())
    for _ in range(n):
        expr = input().strip()
        stack = []
        result = []

        for c in expr:
            if c in '+-*/^':
                stack.append(c)
            elif c == ')':
                result.append(stack.pop())
            elif c not in '( ':
                result.append(c)

        print(''.join(result))


if __name__ == "__main__":
    solve()
