# ============================================================
# Problem: Penguins  (buoi13)
# Source: competitive programming
# ============================================================
# Given n penguins, each belonging to one of three species:
# "Emperor Penguin", "Macaroni Penguin", "Little Penguin".
# Find the species with the most penguins. If tied, any one suffices
# (the code prints the lexicographically first based on map ordering).
#
# Input:
#   - Line 1: n
#   - Next n lines: species name (full name per penguin)
#
# Output:
#   The species name with the highest count.
# ============================================================

def solve():
    n = int(input())
    counts = {}

    for _ in range(n):
        species = input().strip()
        counts[species] = counts.get(species, 0) + 1

    best = max(counts, key=lambda k: counts[k])
    print(best)


if __name__ == "__main__":
    solve()
