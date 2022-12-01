def get_ranked_list_of_elves(file="data/day_1/input.txt"):
    lines = [line.strip() for line in open(file).readlines()]

    elves = [0]
    idx = 0
    for line in lines:
        if line:
            elves[idx] += int(line)
        else:
            idx += 1
            elves.append(0)

    return elves


def challenge_1(file="data/day_1/input.txt"):
    elves = get_ranked_list_of_elves(file)

    max_value = max(elves)
    which_elf = [i for i, e in enumerate(elves) if e == max_value][0]

    print(f"The maximum is {max_value} and it is the {which_elf}th elf.")


def challenge_2(file="data/day_1/input.txt"):
    elves = get_ranked_list_of_elves(file)

    elves.sort()
    total_of_top_three = sum(elves[-3:])

    print(f"The sum of the top three elves is {total_of_top_three}")
