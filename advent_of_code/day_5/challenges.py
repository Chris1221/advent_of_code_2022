def split_line_to_crate(line):
    # Find the indices of the "[" character
    # and find the largest multiple of 4 that
    # fits into that. That will be the index.
    idxs = [i // 4 for i, e in enumerate(list(line)) if e == "["]
    return {str(idx + 1): list(line)[idx * 4 + 1] for idx in idxs}


def crate_reader(lines):
    # Let's start at the bottom and start
    # with a dict to house the piles
    piles = {n: [] for n in lines[-1].strip().split()}

    # Now we'll iterate from the bottom up and add as we go
    # such that the first elment of the list is the top
    # of the pile.
    for line in lines[:-1]:
        for pile, crate in split_line_to_crate(line).items():
            piles[pile].append(crate)

    return piles


def challenge_1(file: str = "data/day_5/input.txt"):
    # First read in the crates. We can do this by reading
    # the lines and stopping when there is an empty char, or
    # the next line starts with the word "move". Let's do both.

    lines = open(file).readlines()

    idx = 0

    for line_idx, line in enumerate(lines):
        if line.strip() == "" and lines[line_idx + 1].startswith("move"):
            crates = crate_reader(lines[:line_idx])
            break

    # Now we'll do the movements. These are basically just pops from
    # one index to another.
    for line in lines:
        if line.startswith("move"):
            _, rep, _, frm, _, to = line.strip().split(" ")
            for r in range(int(rep)):
                crates[to].insert(0, crates[frm].pop(0))

    # Now read off the first element in each pile
    top_elms = [pile[0] for pile in crates.values()]
    print("".join(top_elms))


def challenge_2(file: str = "data/day_5/input.txt"):
    lines = open(file).readlines()

    idx = 0

    for line_idx, line in enumerate(lines):
        if line.strip() == "" and lines[line_idx + 1].startswith("move"):
            crates = crate_reader(lines[:line_idx])
            break

    for line in lines:
        if line.startswith("move"):
            _, rep, _, frm, _, to = line.strip().split(" ")

            # Now get the first rep elements in the list
            elms = crates[frm][: int(rep)]
            crates[to] = elms + crates[to]
            del crates[frm][: int(rep)]

    # Now read off the first element in each pile
    top_elms = [pile[0] for pile in crates.values()]
    print("".join(top_elms))
