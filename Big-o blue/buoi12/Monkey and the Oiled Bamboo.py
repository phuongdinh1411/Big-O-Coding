# ============================================================
# Problem: Monkey and the Oiled Bamboo  (buoi12)
# Source: Kattis
# ============================================================
# A monkey climbs a bamboo with k rungs (at given heights). It starts
# at ground (height 0). On the first step it can jump at most d rungs.
# Each subsequent step it can jump at most d rungs, but loses 1 if
# it climbed more than the previous step's distance (the bamboo is oiled).
# Actually: starting energy = d. Each step reduces energy by 1 if the
# gap to the current rung exceeds the gap of the previous step.
# Find the minimum initial energy d so the monkey can reach the top.
#
# Input:
#   - Line 1: t (test cases)
#   - Each test case:
#       - Line 1: n
#       - Line 2: n integers (rung positions in sorted order)
#
# Output:
#   "Case i: d" for each test case.
#
# Approach:
#   Binary search on d. For a given d, simulate: energy starts at d,
#   decreases by 1 each step where gap > previous gap.
# ============================================================

def check(steps, d):
    energy = d
    prev = 0
    for s in steps:
        gap = s - prev
        if energy < gap:
            return False
        if gap < energy:
            energy -= 1  # energy decreases when gap is smaller
        # actually: energy decreases by 1 each rung regardless;
        # re-reading: energy = d initially, reduced by 1 at each STEP
        # where the step height difference > previous one's
        # The original C++ decrements energy when energy <= gap (the diff)
        prev = s
    return energy >= 0


def simulate(steps, d):
    energy = d
    prev = 0
    for s in steps:
        gap = s - prev
        if energy < gap:
            return False
        if energy == gap:
            pass  # exactly matches, no reduction
        else:
            energy -= (energy <= gap)  # C++ logic: energy-- if energy <= steps[i]-temp
            # This means: if current gap equals energy, reduce energy
        prev = s
    return True


def solve():
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        steps = list(map(int, input().split()))
        steps.sort()

        left, right = 1, 10 ** 7
        ans = right

        while left <= right:
            mid = (left + right) // 2
            energy = mid
            prev = 0
            ok = True
            for s in steps:
                gap = s - prev
                if energy < gap:
                    ok = False
                    break
                if energy > gap:
                    energy -= 1  # oiled: lose 1 if you could have jumped higher
                prev = s

            if ok:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        print(f"Case {case}: {ans}")


if __name__ == "__main__":
    solve()
