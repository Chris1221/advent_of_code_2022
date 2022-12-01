from setuptools import setup

setup(
    name="advent_of_code",
    version="1.0",
    description="Advent of Code 2022",
    author="Chris Cole",
    author_email="chris.c.1221@gmail.com",
    packages=["advent_of_code"],
    entry_points={
        "console_scripts": [
            "aoc = advent_of_code.cli:cli",
        ],
    },
)
