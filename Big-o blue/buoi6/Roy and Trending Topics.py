# ============================================================
# Problem: Roy and Trending Topics  (buoi6)
# Source: HackerEarth
# ============================================================
# Given n topics, each with an old score z and engagement counts:
#   p (posts), l (likes), c (comments), s (shares).
# New score = 50*p + 5*l + 10*c + 20*s.
# A topic is "trending" if its new score > old score.
# Print the top 5 trending topics by (new_score - old_score) descending.
# Ties broken by topic ID ascending.
#
# Input:
#   - Line 1: n
#   - Next n lines: id z p l c s
#
# Output:
#   Top 5 lines: "id new_score"
#
# Approach:
#   Compute change = new_score - old_score for trending topics.
#   Sort by (-change, id) and take first 5.
# ============================================================

def solve():
    n = int(input())
    topics = []

    for _ in range(n):
        parts = list(map(int, input().split()))
        tid, z, p, l, c, s = parts
        new_score = 50 * p + 5 * l + 10 * c + 20 * s
        change = new_score - z
        topics.append((change, tid, new_score))

    # Sort by change descending, then id ascending
    topics.sort(key=lambda x: (-x[0], x[1]))

    for i in range(min(5, len(topics))):
        print(topics[i][1], topics[i][2])


if __name__ == "__main__":
    solve()
