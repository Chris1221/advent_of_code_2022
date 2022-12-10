from numpy import sqrt

FILE: str = "data/day_9/input.txt"

# [X, Y]
DIRS = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}


def diff(t, h):
    if abs(h - t) > 1:
        return int(t + ((h - t) / 2))
    return t


def euc_dist(t, h):
    return sqrt((h[0] - t[0]) ** 2 + (h[1] - t[1]) ** 2)


def get_tail_pos(tail_pos, new_head_pos):
    y_extra = 0
    x_extra = 0
    if euc_dist(tail_pos, new_head_pos) > 2:
        if abs(new_head_pos[0] - tail_pos[0]) > 1:
            y_extra = new_head_pos[1] - tail_pos[1]
        if abs(new_head_pos[1] - tail_pos[1]) > 1:
            x_extra = new_head_pos[0] - tail_pos[0]

        if (y_extra != 0) and (x_extra != 0):
            y_extra = 0
            x_extra = 0

    new_tail_pos = (
        diff(tail_pos[0] + x_extra, new_head_pos[0]),
        diff(tail_pos[1] + y_extra, new_head_pos[1]),
    )

    return new_tail_pos


def challenge_1(file=FILE):

    lines = [i.strip() for i in open(file).readlines()]

    head_pos = (0, 0)
    tail_pos = (0, 0)

    head_positions = [head_pos]
    tail_positions = [tail_pos]

    for line in lines:
        direction, moves = line.split(" ")
        for move in range(int(moves)):
            head_pos = (
                head_pos[0] + DIRS[direction][0],
                head_pos[1] + DIRS[direction][1],
            )
            tail_pos = get_tail_pos(tail_pos, head_pos)
            head_positions.append(head_pos)
            tail_positions.append(tail_pos)

    print(f"A total of {len(set(tail_positions))} were visited")


def challenge_2(file=FILE):
    lines = [i.strip() for i in open(file).readlines()]
    pos = [(0, 0) for i in range(10)]
    tail_positions = []

    for line in lines:
        direction, moves = line.split(" ")

        for move in range(int(moves)):
            new_pos = []
            new_pos.append(
                (
                    pos[0][0] + DIRS[direction][0],
                    pos[0][1] + DIRS[direction][1],
                )
            )
            for i in range(1, len(pos)):
                new_pos.append(get_tail_pos(pos[i], new_pos[i - 1]))

            tail_positions.append(new_pos[-1])
            pos = new_pos

    print(f"A total of {len(set(tail_positions))} were visited")
