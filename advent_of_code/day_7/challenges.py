from dataclasses import dataclass
from typing import Dict

# Visitor methods for an n-tree
# inspired by ANTLR4 :)
class DirectoryStem:
    def __init__(self, name):
        # Optionally instantiate with
        # some children. Or just add them
        # after the fact.

        self.name = name
        self.children = []

    def add_children(self, child):
        assert not isinstance(child, list), "Add them one at a time"
        path = [i for i in child.name.split("/") if i][:-1]

        # Descend the tree of children to find the
        # terminal node

        c = self

        for p in path:
            if p:
                # c = c.get_child("/" + p + "/")
                idx = [n.name for n in c.children].index(c.name + p + "/")
                c = c.children[idx]

        c.children.append(child)

    def find_id(self, id):
        idx = [n.name for n in self.children].index(id)
        return self.children[idx]

    def get_child(self, name):
        path = [i for i in name.split("/") if i][:-1]

        # Descend the tree of children to find the
        # terminal node

        c = self

        path_so_far = "/"

        for p in path:
            if p:
                c = c.find_id(path_so_far + p + "/")
                path_so_far = c.name

        idx = [n.name for n in c.children].index(name)
        if idx is not None:
            return c.children[idx]
        else:
            raise IndexError

    def has_child(self, name):
        try:
            self.get_child(name)
            return True
        except (ValueError, IndexError):
            return False

    def visit(self, directory_sizes={}):
        # Visit the nodes that can be visited (i.e. directory stems)
        # or add up the contributions from individual files

        for child in self.children:
            if isinstance(child, File):
                # Add the number to all parents
                parents = [i for i in child.name.split("/")[:-1] if i]

                start = "/"
                directory_sizes["/"] += child.size

                for p in parents:
                    directory_sizes[start + p + "/"] += child.size
                    start += p + "/"

                # name = "/".join(child.name.split("/")[:-1]) + "/"
                # if name not in directory_sizes:
                #     directory_sizes[name] = 0

                # if name == "/a/e/i":
                #     breakpoint()
                # directory_sizes[name] += child.size

            elif isinstance(child, DirectoryStem):
                # Then recursively visit
                print(f"visiting {child.name}")
                if child.name not in directory_sizes:
                    directory_sizes[child.name] = 0
                directory_sizes = child.visit(directory_sizes)

        return directory_sizes


@dataclass
class File:
    parent: DirectoryStem
    size: int
    name: str


def construct_tree(lines):
    cwd: str = ""

    for line in lines:
        # If it's a cd command then add on to the name
        # of the current directory

        if line.startswith("$"):
            if line.startswith("$ cd"):
                if line.split(" ")[-1] == "..":
                    # Then chop the last element off the cwd
                    cwd = "/".join(cwd.split("/")[:-2]) + "/"
                    continue
                else:
                    cwd += line.split(" ")[-1] + "/"

                # This is just for me
                if cwd == "//":
                    cwd = "/"

                # Special case to initiate the base class
                if cwd == "/":
                    dir = DirectoryStem(cwd)
                    base_dir = dir  # This is to hold the whole thing

                else:
                    # If it's not there already then add it

                    if not base_dir.has_child(cwd):
                        base_dir.add_children(DirectoryStem(cwd))

                    # Switch the context to this one
                    dir = base_dir.get_child(cwd)

            elif line.startswith("$ ls"):
                # Then move on to the size recording portion
                continue

            else:
                raise NotImplementedError("What, did you think this was a whole shell?")

        elif line.startswith("dir"):
            # Then we're adding a directory element to the current
            # cwd context
            _, new_dir = line.split(" ")
            base_dir.add_children(DirectoryStem(cwd + new_dir + "/"))

        else:
            size, name = line.split(" ")
            # We assume this is the size case, but let's check
            try:
                size = int(size)
            except ValueError:
                raise NotImplementedError(f"Something is weird about this line: {line}")

            base_dir.add_children(File(cwd, size, cwd + name))

    return base_dir


def count_all_directory_sizes(tree: DirectoryStem, sizes={}):
    # Start with the base element
    sizes[tree.name] = tree.visit()

    # Now let's start recursing over the children
    for child in tree.children:
        if isinstance(tree, DirectoryStem):
            sizes = count_all_directory_sizes(tree, sizes)

    return sizes


def challenge_1(input="data/day_7/input.txt"):

    lines = [i.strip() for i in open(input).readlines()]
    tree = construct_tree(lines)
    sizes = tree.visit({"/": 0})

    # Filter for sizes <= 100000
    sum = 0
    for k, v in sizes.items():
        if v < 100000:
            sum += v

    print(f"The sum is {sum}")


def challenge_2(input="data/day_7/input.txt"):

    lines = [i.strip() for i in open(input).readlines()]
    tree = construct_tree(lines)
    sizes = tree.visit({"/": 0})

    # unused = 21618835
    # need = 30000000
    # so we must free 30000000 -21618835 = 8381165
    possibilities = []
    for k, v in sizes.items():
        if v + (70000000 - sizes["/"]) >= 30000000:
            possibilities.append(v)

    print(f"The smallest directory is {min(possibilities)}")
