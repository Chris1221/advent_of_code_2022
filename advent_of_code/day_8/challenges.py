import numpy as np
import pandas as pd

FILE: str = "data/day_8/input.txt"
# FILE: str = "data/day_8/test.txt"


def tallest_from(df, direction, i, j, v):

    # If it's from the top, we want to see if its the
    # largest from the top of the dataframe to that
    # element
    # And that there are no other trees of equal height
    if direction == "top":
        # Count down the rows of the j column
        for row_counter in range(i):
            if int(df[j][row_counter]) >= v:
                return False

    if direction == "bottom":
        # Count the opposite direction from the bottom
        for row_counter in reversed(range(i + 1, df.shape[0])):
            if int(df[j][row_counter]) >= v:
                return False

    if direction == "right":

        for col_counter in reversed(range(j + 1, df.shape[1])):

            if int(df[col_counter][i]) >= v:
                return False

    if direction == "left":

        for col_counter in range(j):

            if int(df[col_counter][i]) >= v:
                return False

    return True


def challenge_1(file=FILE):
    # Read the trees into a numpy matrix, then
    # iterate for each i and j to see if that i, j
    # is the max element in the column up, down, side, and side
    # if any of them then set to 1

    lines = [i.strip() for i in open(file).readlines()]
    df = pd.DataFrame([list(i) for i in lines])

    df_index = pd.DataFrame(np.zeros(df.shape))

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            df_index.loc[i, j] = (
                tallest_from(df, "top", i, j, int(df.loc[i, j]))
                or tallest_from(df, "bottom", i, j, int(df.loc[i, j]))
                or tallest_from(df, "right", i, j, int(df.loc[i, j]))
                or tallest_from(df, "left", i, j, int(df.loc[i, j]))
            )

    print(f"The total number of trees visible is {df_index.sum().sum()}")


def scenic_score(df, i, j):

    # For position i, j

    # First look up
    # If it's from the top, we want to see if its the
    # Count down the rows of the j column

    v = int(df.loc[i, j])

    up_score = 0
    for row_counter in reversed(range(i)):
        up_score += 1
        if int(df[j][row_counter]) >= v:
            break

    down_score = 0
    for row_counter in range(i + 1, df.shape[0]):
        down_score += 1
        if int(df[j][row_counter]) >= v:
            break

    right_score = 0
    for col_counter in range(j + 1, df.shape[1]):
        right_score += 1
        if int(df[col_counter][i]) >= v:
            break

    left_score = 0
    for col_counter in reversed(range(j)):
        left_score += 1
        if int(df[col_counter][i]) >= v:
            break

    if i == 1 and j == 2:
        breakpoint()

    return up_score * down_score * right_score * left_score


def challenge_2(file=FILE):
    lines = [i.strip() for i in open(file).readlines()]
    df = pd.DataFrame([list(i) for i in lines])

    df_index = pd.DataFrame(np.zeros(df.shape))

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            df_index.loc[i, j] = scenic_score(df, i, j)

    print(f"The max is {df_index.max().max()}")
