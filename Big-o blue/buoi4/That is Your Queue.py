# ============================================================
# Problem: That is Your Queue  (buoi4)
# Source: UVA
# ============================================================
# A government office has p people and serves them in queue order.
# Perform c queries:
#   N         → Next person served (front of queue moves to back; print them).
#   E person  → Emergency: move 'person' to the front of the queue.
#
# Input:
#   - Multiple test cases until "0 0".
#   - Each test case: p c on one line, then c commands.
#
# Output:
#   "Case X:\n" followed by each N result.
#
# Approach:
#   Simulate with a deque. For E, remove the person and push to front.
#   For very large p (> 2000), only track explicitly moved people.
# ============================================================

from collections import deque


def solve_case(p, c, commands):
    queue = deque(range(1, min(p, 2001) + 1))
    result = []
    next_id = 2001  # Next person not yet in queue

    for cmd in commands:
        parts = cmd.split()
        if parts[0] == 'N':
            front = queue.popleft()
            result.append(front)
            queue.append(front)
        else:
            person = int(parts[1])
            if person <= 2000:
                # Remove from current position
                try:
                    queue.remove(person)
                except ValueError:
                    pass
                queue.appendleft(person)
            else:
                # Person beyond 2000: just add to front
                queue.appendleft(person)

    return result


def main():
    import sys
    lines = sys.stdin.read().split('\n')
    idx = 0
    case = 1

    while idx < len(lines):
        line = lines[idx].strip(); idx += 1
        if not line:
            continue
        parts = line.split()
        p, c = int(parts[0]), int(parts[1])
        if p == 0 and c == 0:
            break

        commands = []
        for _ in range(c):
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            commands.append(lines[idx]); idx += 1

        result = solve_case(p, c, commands)
        print(f"Case {case}:")
        for r in result:
            print(r)
        case += 1


if __name__ == "__main__":
    main()
