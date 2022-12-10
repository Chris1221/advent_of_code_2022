FILE = "data/day_10/input.txt"


def challenge_1(file=FILE):
    lines = [i.strip() for i in open(file).readlines()]

    register = [1]

    for line in lines:
        instruction = line.split(" ")
        register.append(register[-1])

        if len(instruction) == 1:
            continue

        register.append(register[-1] + int(instruction[1]))

    interesting_cycles = [20, 60, 100, 140, 180, 220]

    sum = 0
    for i in interesting_cycles:
        sum += register[i - 1] * i

    print(sum)

    return register


def challenge_2(file=FILE):
    register = challenge_1()

    crt = ""

    pixel = 1

    for i in range(len(register)):
        if pixel in [register[i] - 1, register[i], register[i] + 1]:
            crt += "#"
        else:
            crt += "."

        if i % 40 == 0:
            crt += "\n"
            pixel = 1
        else:
            pixel += 1

    print(crt)
