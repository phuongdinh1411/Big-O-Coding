# ============================================================
# Problem: Dhooom 4  (buoi5)
# Source: competitive programming
# ============================================================
# Starting at value s, you want to reach value f. At each step, you
# can multiply the current value by any of n given multipliers, then
# take modulo 100000. Find the minimum number of steps, or -1 if
# impossible.
#
# Input:
#   - Line 1: s f n
#   - Line 2: n multipliers
#
# Output:
#   Minimum steps, or -1 if impossible.
#
# Approach:
#   BFS on states [0, 99999]. Each state transition: val * mult % 100000.
# ============================================================

from collections import deque


def solve():
    s, f, n = map(int, input().split())
    multipliers = list(map(int, input().split()))

    if s == f:
        print(0)
        return

    dist = [-1] * 100000
    dist[s] = 0
    queue = deque([s])

    while queue:
        cur = queue.popleft()
        for m in multipliers:
            nxt = (cur * m) % 100000
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                if nxt == f:
                    print(dist[nxt])
                    return
                queue.append(nxt)

    print(-1)


if __name__ == "__main__":
    solve()
