from dataclasses import dataclass, field
from typing import List
from tqdm import tqdm
import numpy as np
from collections import deque

FILE = "data/day_11/input.txt"


@dataclass
class Monkey:
    id: int
    items: List[int] = field(default_factory=lambda: deque([]))
    icount: int = 0

    def add_items(self, items):
        for item in items:
            self.items.append(item)

    def set_test(self, line):
        # it's always divisbible so
        self.t = int(line.split(" ")[-1])
        self.test = eval(f"lambda x: (x % {self.t}) == 0")

    def set_true(self, line):
        self.iftrue = int(line.split(" ")[-1])

    def set_false(self, line):
        self.iffalse = int(line.split(" ")[-1])

    def set_operation(self, line):
        formula = line.split("=")[-1].strip()
        self.operation = eval(f"lambda old: {formula}")


@dataclass
class BigMonkey:
    id: int
    items: List[int] = field(default_factory=lambda: deque([]))
    icount: int = 0

    def add_items(self, items):
        for item in items:
            self.items.append(np.log(item))

    def set_true(self, line):
        self.iftrue = int(line.split(" ")[-1])

    def set_false(self, line):
        self.iffalse = int(line.split(" ")[-1])

    def set_operation(self, line):
        formula = line.split("=")[-1].strip()
        old, op, num = formula.split(" ")

        if op == "*":
            self.operation = eval(f"lambda old: old + np.log({num})")
        elif op == "+":
            self.operation = eval(f"lambda old: np.log(np.exp(old) + {num})")

    def set_test(self, line):
        t = line.split(" ")[-1]
        self.test = eval(f"lambda x: (np.exp(x) % {t}) == 0")


def parse_monkeys(file):

    MonkeyDict = {}
    lines = [line.strip() for line in open(file).readlines()]
    monkeys = [idx for idx, line in enumerate(lines) if line.startswith("Monkey")]
    for monkey in monkeys:
        mky = Monkey(int(lines[monkey].split(" ")[-1].replace(":", "")))

        items = [int(i.strip()) for i in lines[monkey + 1].split(": ")[-1].split(",")]
        mky.add_items(items)

        mky.set_operation(lines[monkey + 2])
        mky.set_test(lines[monkey + 3])
        mky.set_true(lines[monkey + 4])
        mky.set_false(lines[monkey + 5])

        MonkeyDict[mky.id] = mky

    return MonkeyDict


def challenge_1(file=FILE):

    # Read in the monkey states and the operations
    monkeys = parse_monkeys(file)
    rounds = 20

    for _ in tqdm(range(rounds)):
        for monkey in monkeys.values():
            while monkey.items:
                monkey.icount += 1
                worry = int(floor(monkey.operation(monkey.items.popleft()) / 3))
                if monkey.test(worry):
                    monkeys[monkey.iftrue].add_items([worry])
                else:
                    monkeys[monkey.iffalse].add_items([worry])

    top, two = sorted([m.icount for m in monkeys.values()])[-2:]
    print(top * two)


def challenge_2(file=FILE):
    monkeys = parse_monkeys(file)
    rounds = 10000

    lcm = np.lcm.reduce([m.t for m in monkeys.values()])

    for _ in tqdm(range(rounds)):
        for monkey in monkeys.values():
            while monkey.items:
                monkey.icount += 1
                # needs to be a log operation so + instead of multiply
                worry = monkey.operation(monkey.items.popleft()) % lcm
                if monkey.test(worry):
                    monkeys[monkey.iftrue].add_items([worry])
                else:
                    monkeys[monkey.iffalse].add_items([worry])

    top, two = sorted([m.icount for m in monkeys.values()])[-2:]
    print(top * two)
