choice_points = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

equiv = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

beats = {
    "X": "C",
    "Y": "A",
    "Z": "B",
}

WIN = 6
DRAW = 3
LOSE = 0


def challenge_1(file: str = "data/day_2/input.txt"):
    lines = [line.strip() for line in open(file).readlines()]

    points = [0]
    i = 0
    for line in lines:
        if line:
            them, us = line.split(" ")
            # Check for draws
            if them == equiv[us]:
                points[i] += DRAW

            # Check for wins
            elif them == beats[us]:
                points[i] += WIN

            points[i] += choice_points[us]

        else:

            points.append(0)
            i += 1

    total_score = sum(points)

    print(f"Your total score is {total_score}")


# Increment the following amounts
end_conditions = {"X": -1, "Y": 0, "Z": 1}


def challenge_2(file: str = "data/day_2/input.txt"):
    lines = [line.strip() for line in open(file).readlines()]

    values = ["A", "B", "C"]

    points = 0
    for line in lines:
        them, condition = line.split(" ")
        increment = end_conditions[condition]

        idx = values.index(them)
        us = idx + increment
        if us >= len(values):
            us = 0

        if increment == 0:  # draw
            points += DRAW

        if increment == 1:  # win
            points += WIN

        points += choice_points[values[us]]

    print(f"Total points: {points}")
