# ============================================================
# Problem: Check Transcription
# Source: Codeforces
# ============================================================
# Given a binary string s (of 0s and 1s) and a text t (lowercase letters),
# count the number of ways to choose non-empty strings r0 ≠ r1 such that
# replacing each '0' in s with r0 and each '1' with r1 produces exactly t.
#
# Input:
#   - Line 1: binary string s (2 ≤ |s| ≤ 10^5)
#   - Line 2: text t (1 ≤ |t| ≤ 10^6)
#
# Output:
#   Number of valid (r0, r1) pairs.
#
# Approach:
#   Let c0, c1 = count of 0s, 1s in s. Constraint: c0*L0 + c1*L1 = len(t).
#   Enumerate possible L0 (length of r0), compute L1, verify consistency.
#   Use polynomial hashing for O(1) substring comparison.
# ============================================================

def solve():
    s = input().strip()
    t = input().strip()

    c0 = s.count('0')
    c1 = s.count('1')
    m = len(t)

    MOD = (1 << 61) - 1
    BASE = 131

    h = [0] * (m + 1)
    pw = [1] * (m + 1)
    for i in range(m):
        h[i + 1] = (h[i] * BASE + ord(t[i])) % MOD
        pw[i + 1] = pw[i] * BASE % MOD

    def get_hash(l, r):  # t[l:r]
        return (h[r] - h[l] * pw[r - l] % MOD + MOD) % MOD

    count = 0

    for L0 in range(1, m + 1):
        if c1 == 0:
            if c0 * L0 == m:
                hash0 = get_hash(0, L0)
                valid = True
                pos = 0
                for ch in s:
                    if pos + L0 > m or get_hash(pos, pos + L0) != hash0:
                        valid = False
                        break
                    pos += L0
                if valid:
                    count += 1
            break if c0 * L0 > m else None
            continue

        remaining = m - c0 * L0
        if remaining <= 0 or remaining % c1 != 0:
            continue
        L1 = remaining // c1
        if L1 <= 0:
            continue

        hash0 = hash1 = None
        valid = True
        pos = 0

        for ch in s:
            if ch == '0':
                curr = get_hash(pos, pos + L0)
                if hash0 is None:
                    hash0 = curr
                elif hash0 != curr:
                    valid = False
                    break
                pos += L0
            else:
                curr = get_hash(pos, pos + L1)
                if hash1 is None:
                    hash1 = curr
                elif hash1 != curr:
                    valid = False
                    break
                pos += L1

        if valid and hash0 != hash1:
            count += 1

    print(count)


if __name__ == "__main__":
    solve()
