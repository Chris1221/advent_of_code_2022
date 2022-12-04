def to_range(elm):
    start, stop = elm.split("-")
    return(set(range(int(start), int(stop)+1)))

def challenge_1(file = "data/day_4/input.txt"):
    nisec = 0
    for line in open(file).readlines():
        pair1, pair2 = line.strip().split(",")
        isec = len(to_range(pair1) & to_range(pair2))
        if (isec == len(to_range(pair1))) or (isec == len(to_range(pair2))):
            nisec += 1
    
    print(f"There are {nisec} total intersections")


def challenge_2(file = "data/day_4/input.txt"):
    nisec = 0
    for line in open(file).readlines():
        pair1, pair2 = line.strip().split(",")
        isec = len(to_range(pair1) & to_range(pair2))
        if isec > 0:
            nisec += 1

    print(f"There are {nisec} total intersections")
