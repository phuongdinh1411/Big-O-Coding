# ============================================================
# Problem: Alphacode
# Source: SPOJ
# ============================================================
# Alice encodes messages by replacing each letter with its position:
# A=1, B=2, ..., Z=26. Bob receives a string of digits and wants to
# know how many different decodings are possible.
# For example "25114" can be decoded as:
#   BEAN, BEAAD, YAAD, YAN, YKD, BEKD  → 6 ways.
#
# Input:
#   - Multiple lines each with a digit string (no leading zeros).
#   - Input ends with "0".
#
# Output:
#   For each string, the number of decodings (fits in 64-bit signed int).
#
# Approach:
#   dp[i] = ways to decode first i characters.
#   Single digit (1-9):  dp[i] += dp[i-1]
#   Two digits  (10-26): dp[i] += dp[i-2]
# ============================================================

def count_decodings(s):
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        two = int(s[i - 2:i])
        if 10 <= two <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


def main():
    while True:
        s = input().strip()
        if s == '0':
            break
        print(count_decodings(s))


if __name__ == "__main__":
    main()
