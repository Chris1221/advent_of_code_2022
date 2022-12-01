import argparse
from importlib import import_module


def cli():
    parser = argparse.ArgumentParser("Advent of code 2022")
    parser.add_argument("-d", "--day", type=int, required=True)
    parser.add_argument("-c", "--challenge", type=int, required=True)

    args = parser.parse_args()

    # Get a list of submodules
    submodules = [m for m in dir() if m.startswith("day_")]

    try:
        # Import the challenge of interest from the submodule
        day = import_module(f"advent_of_code.day_{args.day}")
        challenge = getattr(day, f"c_{args.challenge}")
        # Run the challenge
        challenge()
    except (ModuleNotFoundError, AttributeError):
        print(f"Day {args.day} or challenge {args.challenge} not found.")
