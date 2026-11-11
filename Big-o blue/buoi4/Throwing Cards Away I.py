# ============================================================
# Problem: Throwing Cards Away I  (buoi4)
# Source: UVA
# ============================================================
# You have a deck of n cards (numbered 1..n, top to bottom).
# Repeatedly: discard the top card, move the next top card to the bottom.
# Print which cards were discarded (in discard order) and the remaining card.
#
# Input:
#   - Multiple test cases until n = 0.
#   - Each test case: n on its own line.
#
# Output:
#   "Discarded cards: c1, c2, ..."
#   "Remaining card: c"
#
# Approach:
#   Simulate with a deque.
# ============================================================

from collections import deque


def solve():
    while True:
        n = int(input())
        if n == 0:
            break

        deck = deque(range(1, n + 1))
        discarded = []

        while len(deck) >= 2:
            discarded.append(deck.popleft())   # discard top
            deck.append(deck.popleft())         # move top to bottom

        if discarded:
            print("Discarded cards: " + ', '.join(map(str, discarded)))
        else:
            print("Discarded cards:")
        print(f"Remaining card: {deck[0]}")


if __name__ == "__main__":
    solve()
