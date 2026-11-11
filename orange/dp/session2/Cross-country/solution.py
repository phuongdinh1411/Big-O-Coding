# ============================================================
# Problem: Cross-country
# Source: SPOJ
# ============================================================
# Agnes participates in cross-country races following a route of
# checkpoints. Tom (and others) also have routes. Tom scores one
# point each time he meets Agnes at a checkpoint (after a previous
# meeting, both must move to their next checkpoint before scoring again).
# Find the maximum number of times Tom can meet Agnes.
#
# Input:
#   - d data sets.
#   - Each data set:
#       - Agnes' route: integers ending with 0.
#       - Tom's routes: each ending with 0; dataset ends with a line "0".
#   - Checkpoints are integers in [1, 1000], routes have 2–2000 checkpoints.
#
# Output:
#   For each data set: maximum meetings (= LCS length) over all of Tom's routes.
#
# Approach:
#   Maximum meetings = LCS(Agnes' route, Tom's route).
#   Both follow their cards in order, score when at the same checkpoint.
# ============================================================

def lcs_len(a, b):
    m, n = len(a), len(b)
    prev = [0] * (n + 1)
    for i in range(m):
        curr = [0] * (n + 1)
        for j in range(n):
            if a[i] == b[j]:
                curr[j + 1] = prev[j] + 1
            else:
                curr[j + 1] = max(prev[j + 1], curr[j])
        prev = curr
    return prev[n]


def solve():
    d = int(input())

    for _ in range(d):
        agnes = []
        for x in input().split():
            v = int(x)
            if v == 0:
                break
            agnes.append(v)

        best = 0
        while True:
            parts = input().split()
            if parts[0] == '0':
                break
            tom = []
            for x in parts:
                v = int(x)
                if v == 0:
                    break
                tom.append(v)
            best = max(best, lcs_len(agnes, tom))

        print(best)


if __name__ == "__main__":
    solve()
