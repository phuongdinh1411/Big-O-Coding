# ============================================================
# Problem: Ferry Loading III  (buoi4)
# Source: UVA
# ============================================================
# A ferry shuttles between left and right banks. It starts at the
# left bank at time 0 and alternates sides. Each crossing takes
# 'trav' minutes. The ferry can carry at most 'cap' cars per trip.
# Cars arrive at specific times on either bank.
# Output the time each car arrives at their destination bank.
#
# Input:
#   - Line 1: number of test cases
#   - Each test case:
#       - Line 1: cap trav m  (capacity, travel time, number of cars)
#       - Next m lines: t side  ("left" or "right")
#   - Blank line between test cases.
#
# Output:
#   For each car (in input order), its arrival time. Blank line between cases.
#
# Approach:
#   Simulate: ferry alternates sides, loads up to cap waiting cars per trip.
#   When no cars are waiting, fast-forward to next arrival.
# ============================================================

from collections import deque


def solve_case(cap, trav, m, cars):
    left_q = deque()   # (arrival_time, car_index)
    right_q = deque()
    ans = [0] * m
    car_idx = 0
    time = 0
    side = 0  # 0 = left, 1 = right

    # Sort cars into their queues (cars given in arrival order already)
    left_cars = deque()
    right_cars = deque()
    for i, (t, s) in enumerate(cars):
        if s == "left":
            left_cars.append((t, i))
        else:
            right_cars.append((t, i))

    while left_cars or left_q or right_cars or right_q:
        # Move newly arrived cars into waiting queue
        while left_cars and left_cars[0][0] <= time:
            left_q.append(left_cars.popleft())
        while right_cars and right_cars[0][0] <= time:
            right_q.append(right_cars.popleft())

        # If nobody waiting, fast-forward
        if (side == 0 and not left_q) or (side == 1 and not right_q):
            if side == 0 and not left_q:
                if left_cars:
                    time = left_cars[0][0]
                elif right_q or right_cars:
                    side = 1
                    time += trav
                continue
            if side == 1 and not right_q:
                if right_cars:
                    time = right_cars[0][0]
                elif left_q or left_cars:
                    side = 0
                    time += trav
                continue

        # Load and cross
        loaded = 0
        if side == 0:
            while left_q and loaded < cap:
                _, idx = left_q.popleft()
                ans[idx] = time + trav
                loaded += 1
            side = 1
        else:
            while right_q and loaded < cap:
                _, idx = right_q.popleft()
                ans[idx] = time + trav
                loaded += 1
            side = 0
        time += trav

    return ans


def main():
    import sys
    data = sys.stdin.read().split('\n')
    idx = 0
    n = int(data[idx]); idx += 1
    first = True

    for _ in range(n):
        while idx < len(data) and not data[idx].strip():
            idx += 1
        cap, trav, m = map(int, data[idx].split()); idx += 1
        cars = []
        for _ in range(m):
            parts = data[idx].split(); idx += 1
            cars.append((int(parts[0]), parts[1]))

        result = solve_case(cap, trav, m, cars)

        if not first:
            print()
        first = False
        for t in result:
            print(t)


if __name__ == "__main__":
    main()
