def common(
    nbuffer,
    file="data/day_6/input.txt",
):
    # Read in the input
    data = open(file).read().strip()

    # We're going to make an n digit
    # signal set and traverse the list
    # to see when the signal set is
    # actually n letter long
    signal = set()

    buffer = []
    for idx, char in enumerate(list(data)):

        if len(buffer) < nbuffer:
            buffer.append(char)
        else:
            buffer.pop(0)
            buffer.append(char)

        # 4 unique characters present in buffer
        if len(set(buffer)) == nbuffer:
            print(f"The index is {idx+1}")
            break


def challenge_1():
    common(4)


def challenge_2():
    common(14)
