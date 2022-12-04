def get_score(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def get_intersect(list1, list2):
    isec = list(set(list1) & set(list2))
    assert len(isec) == 1, "More than 1 in common"
    return isec[0]


def get_intersect3(list1, list2, list3):
    isec = list(set(list1) & set(list2) & set(list3))
    try:
        assert len(isec) == 1
    except AssertionError:
        breakpoint()
    return isec[0]


def challenge_1(file: str = "data/day_3/input.txt"):
    score = 0
    for line in open(file).readlines():
        chars = list(line.strip())
        first_half, second_half = chars[: len(chars) // 2], chars[len(chars) // 2 :]
        score += get_score(get_intersect(first_half, second_half))

    print(f"Total score is {score}")


def challenge_2(file: str = "data/day_3/input.txt"):
    score = 0
    i = 0

    group = []
    for line in open(file).readlines():
        chars = list(line.strip())

        group.append(chars)

        if i == 2:
            score += get_score(get_intersect3(*group))
            group = []
            i = 0
            continue

        i += 1

    print(f"Total score is {score}")
