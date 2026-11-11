# ============================================================
# Problem: Mass of Molecule  (buoi4)
# Source: UVA / competitive programming
# ============================================================
# Given a chemical formula string (containing C, H, O, digits, parentheses),
# compute the molecular mass. Atomic masses: C=12, H=1, O=16.
# A number after an atom or closing parenthesis multiplies its count.
# Example: "C6H12O6" → 6*12 + 12*1 + 6*16 = 180.
#
# Input:
#   - A single chemical formula string.
#
# Output:
#   Total molecular mass.
#
# Approach:
#   Use a stack. Parse left to right:
#   - Atom: push its mass.
#   - Number: multiply the top of stack.
#   - '(': push sentinel.
#   - ')': pop until sentinel, sum, push sum.
# ============================================================

def solve():
    s = input().strip()
    atom_mass = {'C': 12, 'H': 1, 'O': 16}
    stack = []
    i = 0

    while i < len(s):
        c = s[i]
        if c in atom_mass:
            stack.append(atom_mass[c])
            i += 1
        elif c == '(':
            stack.append('(')
            i += 1
        elif c == ')':
            i += 1
            total = 0
            while stack[-1] != '(':
                total += stack.pop()
            stack.pop()  # remove '('
            stack.append(total)
        elif c.isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            stack[-1] *= num
        else:
            i += 1

    print(sum(stack))


if __name__ == "__main__":
    solve()
