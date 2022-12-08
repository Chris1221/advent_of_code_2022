import numpy as np
import pandas as pd

FILE: str = "data/day_8/input.txt"


def tallest_from(df, direction, i, j, v):

    # If it's from the top, we want to see if its the
    # largest from the top of the dataframe to that
    # element
    # And that there are no other trees of equal height
    if direction == "top":
        # Count down the rows of the j column
        for row_counter in range(i):
            if df[j][row_counter] >= v:
                return False

    if direction == "bottom":
        # Count the opposite direction from the bottom

        for row_counter in reversed(range(i, df.shape[0])):

            if df[j][row_counter] >= v:
                return False

    if direction == "right":

        for col_counter in reversed(range(j, df.shape[1])):

            if df[i][col_counter] >= v:
                return False

    if direction == "left":

        for col_counter in range(j, df.shape[1]):

            if df[i][col_counter] >= v:
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
                tallest_from(df, "top", i, j, df.loc[i, j])
                or tallest_from(df, "bottom", i, j, df.loc[i, j])
                or tallest_from(df, "right", i, j, df.loc[i, j])
                or tallest_from(df, "left", i, j, df.loc[i, j]),
            )

    sdfasdf


def challenge_2(file=FILE):
    pass
