# ============================================================
# Problem: Possible Friends  (buoi10)
# Source: competitive programming
# ============================================================
# Given n people and a friendship matrix (Y/N), find the person who
# has the most "possible friends": people who are not already friends
# but have exactly one mutual friend (distance 2 in the friendship graph).
# Output: person_index count
#
# Input:
#   - Line 1: n
#   - Next n lines: a row of Y/N strings (friendship matrix row)
#
# Output:
#   For each test case: "person count" (0-indexed person with most possible friends).
#
# Approach:
#   Floyd-Warshall with distance matrix. Count nodes at distance 2.
# ============================================================

def solve():
    n = int(input())

    for _ in range(n):
        first_row = input().split()
        m = len(first_row[0])
        rows = [first_row[0]]
        for _ in range(m - 1):
            rows.append(input().split()[0])

        INF = 3
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
        for i in range(m):
            for j in range(m):
                if rows[i][j] == 'Y':
                    dist[i][j] = 1
                    dist[j][i] = 1

        # Floyd-Warshall
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        best_count = 0
        best_person = 0
        for i in range(m):
            count = sum(1 for j in range(m) if dist[i][j] == 2)
            if count > best_count:
                best_count = count
                best_person = i

        print(best_person, best_count)


if __name__ == "__main__":
    solve()
