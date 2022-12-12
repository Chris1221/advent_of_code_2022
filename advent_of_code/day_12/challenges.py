import numpy as np
from collections import deque

FILE = "data/day_12/input.txt"

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def create_map(file, all_a=False):
    lines = [line.strip() for line in open(file).readlines()]

    first = True
    for line in lines:
        row = [ord(l) for l in line]
        if first:
            map = np.array(row)
            first = False
        else:
            map = np.vstack((map, row))

    start = np.where(map == 83)  # ord("S")
    stop = np.where(map == 69)

    start = [(start[0][0], start[1][0])]

    if all_a:
        for x, y in zip(*np.where(map == ord("a"))):
            start.append((x, y))

    return map, start, stop


def can_move(map, new, old):
    try:
        if map[new] == 69:
            if ord("z") - map[old] <= 1:
                return True
        elif (map[new] - map[old]) <= 1:
            return True
        elif map[old] == 83:
            if map[new] - ord("a") <= 1:
                return True
    except IndexError:
        return False

    return False


def BFS(map, start, stop):
    seen = set(start)
    queue = deque([(s, 0) for s in start])
    while queue:
        (cx, cy), step = queue.popleft()

        if map[(cx, cy)] == 69:
            return step

        for dx, dy in MOVES:
            new = (cx + dx, cy + dy)

            if can_move(map, new, (cx, cy)) and (new not in seen):
                queue.append((new, step + 1))
                seen.add(new)


def challenge_1(file=FILE):
    map, start, stop = create_map(file, all_a=False)
    print(BFS(map, start, stop))


def challenge_2(file=FILE):
    map, start, stop = create_map(file, all_a=True)
    print(BFS(map, start, stop))
