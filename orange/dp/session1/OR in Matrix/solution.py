# ============================================================
# Problem: OR in Matrix
# Source: Codeforces
# ============================================================
# Nam has an m×n binary matrix A. Matrix B is derived as:
#   B[i][j] = (OR of all elements in row i of A)  OR
#              (OR of all elements in column j of A)
# Given B, reconstruct any valid A, or report "NO" if impossible.
#
# Input:
#   - Line 1: m n
#   - Next m lines: n integers (0 or 1) forming matrix B.
#
# Output:
#   "NO" if impossible.
#   "YES" followed by the m×n matrix A otherwise.
#
# Approach:
#   If B[i][j]=0 → both row i and column j of A must be all zeros.
#   Start A with all 1s, zero out rows/cols forced by B[i][j]=0.
#   Verify reconstructed A produces B; print YES/NO accordingly.
# ============================================================

def solve():
    m, n = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(m)]

    zero_rows = set()
    zero_cols = set()

    for i in range(m):
        for j in range(n):
            if B[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    A = [[0 if (i in zero_rows or j in zero_cols) else 1
          for j in range(n)] for i in range(m)]

    # Verify
    row_or = [any(A[i]) for i in range(m)]
    col_or = [any(A[i][j] for i in range(m)) for j in range(n)]

    for i in range(m):
        for j in range(n):
            expected = 1 if (row_or[i] or col_or[j]) else 0
            if expected != B[i][j]:
                print("NO")
                return

    print("YES")
    for row in A:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    solve()
