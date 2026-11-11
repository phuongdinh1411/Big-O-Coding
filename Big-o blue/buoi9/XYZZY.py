# ============================================================
# Problem: XYZZY  (buoi9)
# Source: UVA
# ============================================================
# A dungeon has n rooms. Each room has an energy value (can be negative).
# You start in room 1 with 100 energy; reaching room n with energy > 0 wins.
# Rooms have doors leading to other rooms. Traveling between rooms costs/gives
# energy based on the destination room's value.
# If you can enter a positive-energy cycle reachable from room 1 that also
# leads to room n, you can always win ("winnable"), otherwise "hopeless".
#
# Input:
#   - Multiple test cases until n = -1.
#   - Each test case:
#       - Line 1: n
#       - Next n lines: energy_i num_doors door1 door2 ...
#
# Output:
#   "winnable" or "hopeless" for each test case.
#
# Approach:
#   Modified Bellman-Ford maximizing energy. If energy at room n > 0,
#   output "winnable".
# ============================================================

def solve():
    while True:
        n = int(input())
        if n == -1:
            break

        energy = [0] * (n + 1)
        doors = [[] for _ in range(n + 1)]

        for i in range(1, n + 1):
            parts = list(map(int, input().split()))
            energy[i] = parts[0]
            num = parts[1]
            for k in range(num):
                doors[i].append(parts[2 + k])

        # Build edges: entering room v from room u gives energy[v]
        edges = []
        for u in range(1, n + 1):
            for v in doors[u]:
                edges.append((u, v, energy[v]))

        # Bellman-Ford maximizing energy (start at room 1 with 100 + energy[1])
        INF = float('-inf')
        level = [INF] * (n + 1)
        level[1] = 100 + energy[1]

        for _ in range(n - 1):
            for u, v, e in edges:
                if level[u] > 0 and level[u] + e > level[v]:
                    level[v] = level[u] + e

        # Extra passes to propagate positive cycles
        for _ in range(n):
            for u, v, e in edges:
                if level[u] > 0 and level[u] + e > level[v]:
                    level[v] = level[u] + e

        print("winnable" if level[n] > 0 else "hopeless")


if __name__ == "__main__":
    solve()
