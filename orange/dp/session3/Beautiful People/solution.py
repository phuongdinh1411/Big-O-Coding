# ============================================================
# Problem: Beautiful People
# Source: Codeforces
# ============================================================
# A club has N members each with strength Si and beauty Bi.
# Member i hates member j if (Si < Sj AND Bi > Bj) OR (Si > Sj AND Bi < Bj).
# Select the maximum subset of members such that no two hate each other
# (i.e., the selected members can be ordered so both S and B are non-decreasing).
# Output: size of the largest group and the original indices of its members.
#
# Input:
#   - Line 1: N (2 ≤ N ≤ 100,000)
#   - Next N lines: Si Bi
#
# Output:
#   - Line 1: maximum members
#   - Line 2: their 1-indexed positions.
#
# Approach:
#   Sort by S ascending; ties by B descending (prevent same-S double-count).
#   Find LIS on B values using binary search + parent tracking.
# ============================================================

import bisect


def solve():
    n = int(input())
    members = []
    for i in range(n):
        s, b = map(int, input().split())
        members.append((s, b, i + 1))

    members.sort(key=lambda x: (x[0], -x[1]))
    beauties = [m[1] for m in members]

    tails = []
    tail_idx = []
    predecessor = [-1] * n
    lis_pos = [0] * n

    for i in range(n):
        b = beauties[i]
        pos = bisect.bisect_left(tails, b)
        if pos == len(tails):
            tails.append(b)
            tail_idx.append(i)
        else:
            tails[pos] = b
            tail_idx[pos] = i
        lis_pos[i] = pos
        if pos > 0:
            predecessor[i] = tail_idx[pos - 1]

    lis_len = len(tails)
    path = []
    idx = tail_idx[-1]
    while idx != -1:
        path.append(members[idx][2])
        idx = predecessor[idx]
    path.reverse()

    print(lis_len)
    print(' '.join(map(str, path)))


if __name__ == "__main__":
    solve()
