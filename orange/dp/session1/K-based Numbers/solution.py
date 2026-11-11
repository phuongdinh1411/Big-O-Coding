# ============================================================
# Problem: K-based Numbers
# Source: Timus Online Judge
# ============================================================
# Count N-digit numbers in base K that do NOT contain two successive
# zeros. Numbers must have exactly N digits (no leading zero allowed).
#
# Example: in base 10 with N=2: "00" is not 2-digit; "10","20",…,"90"
# all contain 0 but not "00", so all 90 two-digit numbers are valid.
#
# Input:
#   - Two lines: N then K  (2 ≤ K ≤ 10, N ≥ 2, N+K ≤ 18)
#
# Output:
#   The count of valid N-digit K-based numbers.
#
# Approach:
#   dp with two states per position:
#     end_zero    = count of valid i-digit numbers ending with 0
#     end_nonzero = count of valid i-digit numbers ending with non-zero
#   Transitions:
#     new_end_zero    = end_nonzero          (only non-zero can precede 0)
#     new_end_nonzero = (end_zero + end_nonzero) * (K-1)
# ============================================================

def solve():
    n = int(input())
    k = int(input())

    end_zero = 0
    end_nonzero = k - 1  # first digit: 1 .. k-1

    for _ in range(2, n + 1):
        end_zero, end_nonzero = end_nonzero, (end_zero + end_nonzero) * (k - 1)

    print(end_zero + end_nonzero)


if __name__ == "__main__":
    solve()
