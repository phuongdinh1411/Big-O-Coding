# ============================================================
# Problem: Search Engine  (buoi14)
# Source: competitive programming
# ============================================================
# Given a dictionary of n words each with a weight, and q prefix queries,
# for each query return the maximum weight among all words starting with
# the given prefix. Output -1 if no such word exists.
#
# Input:
#   - Line 1: n q
#   - Next n lines: word weight
#   - Next q lines: prefix query
#
# Output:
#   For each query: max weight with that prefix, or -1.
#
# Approach:
#   Trie where each node stores the max weight in its subtree.
#   Query: traverse trie to the prefix node, return its max weight.
# ============================================================

def solve():
    n, q = map(int, input().split())

    # Trie as dict: node = {'children': {}, 'max_weight': -1}
    root = {'children': {}, 'max_weight': -1}

    def insert(word, weight):
        node = root
        for c in word:
            if c not in node['children']:
                node['children'][c] = {'children': {}, 'max_weight': -1}
            node = node['children'][c]
            node['max_weight'] = max(node['max_weight'], weight)

    def query(prefix):
        node = root
        for c in prefix:
            if c not in node['children']:
                return -1
            node = node['children'][c]
        return node['max_weight']

    for _ in range(n):
        parts = input().split()
        word, weight = parts[0], int(parts[1])
        insert(word, weight)

    for _ in range(q):
        prefix = input().strip()
        print(query(prefix))


if __name__ == "__main__":
    solve()
