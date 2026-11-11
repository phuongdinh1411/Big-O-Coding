# ============================================================
# Problem: Isenbaev's Number  (buoi13)
# Source: Codeforces
# ============================================================
# Isenbaev (a famous competitive programmer) has number 0. His teammates
# in any contest have number 1. Teammates of his teammates have number 2, etc.
# Given n teams of 3 members each, compute each person's Isenbaev's number.
# Print "undefined" if not reachable.
#
# Input:
#   - Line 1: n
#   - Next n lines: three names (team members)
#
# Output:
#   For each known person (sorted alphabetically): "name number".
#
# Approach:
#   BFS from "Isenbaev". Each team member within the same team is adjacent
#   (distance + 1). Propagate through all teams.
# ============================================================

from collections import deque, defaultdict


def solve():
    n = int(input())
    teams = []
    people = set()
    people.add("Isenbaev")

    for _ in range(n):
        parts = input().split()
        teams.append(parts)
        for p in parts:
            people.add(p)

    # Build adjacency: within same team, all 3 are connected
    adj = defaultdict(set)
    for team in teams:
        for i in range(3):
            for j in range(3):
                if i != j:
                    adj[team[i]].add(team[j])

    dist = {"Isenbaev": 0}
    queue = deque(["Isenbaev"])

    while queue:
        person = queue.popleft()
        for nb in adj[person]:
            if nb not in dist:
                dist[nb] = dist[person] + 1
                queue.append(nb)

    for person in sorted(people):
        if person in dist:
            print(person, dist[person])
        else:
            print(person, "undefined")


if __name__ == "__main__":
    solve()
