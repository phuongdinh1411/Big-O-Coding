# ============================================================
# Problem: Arbitrage  (buoi10)
# Source: UVA
# ============================================================
# Given n currencies and exchange rates between them, determine if
# arbitrage is possible (can you start with 1 USDollar and end with
# more than 1 USDollar through currency conversions)?
#
# Input:
#   - Multiple test cases until n = 0.
#   - Each test case:
#       - Line 1: n (currencies)
#       - Next n lines: currency name
#       - Line: m (exchange rates)
#       - Next m lines: src rate dst
#
# Output:
#   "Case X: Yes" or "Case X: No"
#
# Approach:
#   Floyd-Warshall maximizing product of rates.
#   If dist[USD][USD] > 1.0, arbitrage is possible.
# ============================================================

def solve():
    case = 0
    while True:
        n = int(input())
        if n == 0:
            break
        case += 1

        names = []
        name_map = {}
        for i in range(n):
            name = input().strip()
            names.append(name)
            name_map[name] = i

        dist = [[0.0] * n for _ in range(n)]

        m = int(input())
        for _ in range(m):
            parts = input().split()
            src, rate, dst = parts[0], float(parts[1]), parts[2]
            u, v = name_map[src], name_map[dst]
            dist[u][v] = max(dist[u][v], rate)

        # Floyd-Warshall (maximize product)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] * dist[k][j] > dist[i][j]:
                        dist[i][j] = dist[i][k] * dist[k][j]

        usd = name_map.get("USDollar", -1)
        if usd != -1 and dist[usd][usd] > 1.0:
            print(f"Case {case}: Yes")
        else:
            print(f"Case {case}: No")


if __name__ == "__main__":
    solve()
