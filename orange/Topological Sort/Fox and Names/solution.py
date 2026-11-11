# ============================================================
# Problem: Fox and Names
# Source: Codeforces
# ============================================================
# n authors' names are listed in a paper. They are sorted
# lexicographically under some reordering of the 26 Latin letters.
# Find any valid alphabet ordering, or print "Impossible".
#
# Comparing adjacent names gives ordering constraints on characters:
# first differing position i → name1[i] must precede name2[i].
# If name2 is a strict prefix of name1, it's always impossible.
#
# Input:
#   - Line 1: n (1 ≤ n ≤ 100)
#   - Next n lines: a name (1 ≤ |name| ≤ 100, lowercase)
#
# Output:
#   A permutation of 'a'-'z' if possible, otherwise "Impossible".
#
# Approach:
#   Build a directed graph from constraints, run Kahn's topological sort.
#   A cycle ↔ "Impossible".
# ============================================================

from collections import deque, defaultdict


def solve():
    n = int(input())
    names = [input().strip() for _ in range(n)]

    graph = defaultdict(set)
    in_degree = {chr(ord('a') + i): 0 for i in range(26)}

    for i in range(n - 1):
        s1, s2 = names[i], names[i + 1]
        found = False
        for j in range(min(len(s1), len(s2))):
            if s1[j] != s2[j]:
                if s2[j] not in graph[s1[j]]:
                    graph[s1[j]].add(s2[j])
                    in_degree[s2[j]] += 1
                found = True
                break
        if not found and len(s1) > len(s2):
            print("Impossible")
            return

    queue = deque(c for c in in_degree if in_degree[c] == 0)
    result = []

    while queue:
        c = queue.popleft()
        result.append(c)
        for nb in graph[c]:
            in_degree[nb] -= 1
            if in_degree[nb] == 0:
                queue.append(nb)

    if len(result) != 26:
        print("Impossible")
    else:
        print(''.join(result))


if __name__ == "__main__":
    solve()
