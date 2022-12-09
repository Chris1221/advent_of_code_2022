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


def get_new_pos(tail_pos, head_pos, direction):

    # Incremement head_pos by direction
    new_head_pos = (
        head_pos[0] + DIRS[direction][0],
        head_pos[1] + DIRS[direction][1],
    )

    # Check if tail position is lagging

    # Check if an additional diagonal move
    # is needed

    y_extra = 0
    x_extra = 0
    if euc_dist(tail_pos, new_head_pos) > 2:
        # whichever direction it moved in
        # add one to the other direction

        if abs(new_head_pos[0] - tail_pos[0]) > 1:
            y_extra = new_head_pos[1] - tail_pos[1]
        if abs(new_head_pos[1] - tail_pos[1]) > 1:
            x_extra = new_head_pos[0] - tail_pos[0]

    new_tail_pos = (
        diff(tail_pos[0] + x_extra, new_head_pos[0]),
        diff(tail_pos[1] + y_extra, new_head_pos[1]),
    )

    # head_positions.append(new_head_pos)
    # tail_positions.append(new_tail_pos)

    # if tail_pos == (2, 4):
    #    breakpoint()

    # print(
    #     f"""
    # The instruction was {line}:
    #     Old_positions: {head_pos}, {tail_pos}
    #     New positions: {new_head_pos}, {new_tail_pos}
    # """
    # )

    # head_pos = new_head_pos
    # tail_pos = new_tail_pos

    return new_tail_pos, new_head_pos


def challenge_1(file=FILE):

    lines = [i.strip() for i in open(file).readlines()]

    head_pos = (0, 0)
    tail_pos = (0, 0)

    head_positions = [head_pos]
    tail_positions = [tail_pos]

    for line in lines:
        direction, moves = line.split(" ")

        for move in range(int(moves)):
            tail_pos, head_pos = get_new_pos(tail_pos, head_pos, direction)
            head_positions.append(head_pos)
            tail_positions.append(tail_pos)

    print(f"A total of {len(set(tail_positions))} were visited")


def challenge_2(file=FILE):

    lines = [i.strip() for i in open(file).readlines()]

    tail_pos = [(0, 0) for i in range(10)]
    head_pos = (0, 0)

    head_positions = [head_pos]
    tail_positions = [knots]

    for line in lines:
        direction, moves = line.split(" ")

        for move in range(int(moves)):

            # First get the new head position like normal

            new_tail_pos, new_head_pos = get_new_pos(tail_pos[0], head_pos, direction)
            new_tail_pos = [new_tail_pos]
            # And then go through the list

            for idx, cur_tail_pos in enumerate(tail_pos[1:]):
                current_new_tail_post, new_

                head_positions.append(head_pos)
                tail_positions.append(tail_pos)

    pass
