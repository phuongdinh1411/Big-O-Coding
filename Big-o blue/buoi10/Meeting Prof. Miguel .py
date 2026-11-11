# ============================================================
# Problem: Meeting Prof. Miguel  (buoi10)
# Source: UVA
# ============================================================
# Two people (Y and N) want to meet at some city. They travel on
# different networks of roads (Y-roads and N-roads). Roads can be
# one-directional ('D') or bidirectional ('B'). City names are single
# uppercase letters. Find the minimum total cost and all cities where
# they can meet. Print "You will never meet." if impossible.
#
# Input:
#   - Multiple test cases until n = 0.
#   - Each test case:
#       - Line 1: n (roads)
#       - Next n lines: person dir src dst cost  (Y/N, D/B, letter, letter, int)
#       - Last line: start_Y start_N
#
# Output:
#   "min_cost city1 city2 ..." or "You will never meet."
#
# Approach:
#   Floyd-Warshall separately for Y's and N's graphs.
#   For each city c: total = dist_Y[start_Y][c] + dist_N[start_N][c].
#   Find minimum and all cities achieving it.
# ============================================================

def solve():
    while True:
        n = int(input())
        if n == 0:
            break

        INF = 10 ** 9
        dist_y = [[INF] * 26 for _ in range(26)]
        dist_n = [[INF] * 26 for _ in range(26)]

        for i in range(26):
            dist_y[i][i] = dist_n[i][i] = 0

        for _ in range(n):
            parts = input().split()
            person, direction, src, dst, cost = parts[0], parts[1], parts[2], parts[3], int(parts[4])
            u, v = ord(src) - 65, ord(dst) - 65

            if person == 'Y':
                dist_y[u][v] = min(dist_y[u][v], cost)
                if direction == 'B':
                    dist_y[v][u] = min(dist_y[v][u], cost)
            else:
                dist_n[u][v] = min(dist_n[u][v], cost)
                if direction == 'B':
                    dist_n[v][u] = min(dist_n[v][u], cost)

        # Floyd-Warshall
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist_y[i][k] + dist_y[k][j] < dist_y[i][j]:
                        dist_y[i][j] = dist_y[i][k] + dist_y[k][j]
                    if dist_n[i][k] + dist_n[k][j] < dist_n[i][j]:
                        dist_n[i][j] = dist_n[i][k] + dist_n[k][j]

        sy_str, sn_str = input().split()
        sy, sn = ord(sy_str) - 65, ord(sn_str) - 65

        best = INF
        meeting = []
        for c in range(26):
            total = dist_y[sy][c] + dist_n[sn][c]
            if total < best:
                best = total
                meeting = [c]
            elif total == best:
                meeting.append(c)

        if best == INF:
            print("You will never meet.")
        else:
            cities = ' '.join(chr(c + 65) for c in sorted(meeting))
            print(best, cities)


if __name__ == "__main__":
    solve()
