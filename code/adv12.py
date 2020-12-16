
def myRevereseLookup(d: dict, val: int) -> str:
    for t in d.items():
        if t[1] == val:
            return str(t[0])
    return None

def updateFacingDir(b, t: tuple) -> None:
    lookupDict = dict({"N": 0, "E": 90, "S": 180, "W": 270})
    degrees = lookupDict.get(b.facingDir)

    if t[0] == 'R':
        degrees = (degrees + t[1]) % 360
    elif t[0] == 'L':
        degrees = (degrees - t[1]) % 360

    b.facingDir = myRevereseLookup(lookupDict, degrees) # No built-in?
    return

def moveForward(b, t: tuple) -> None:
    if b.facingDir == 'N' or b.facingDir == 'S':
        if b.facingDir == 'N':
            b.relPosNorth += t[1]
        else:
            b.relPosNorth -= t[1]
    else:
        if b.facingDir == 'E':
            b.relPosEast += t[1]
        else:
            b.relPosEast -= t[1]
    return


def moveBoat(b, w, t: tuple) -> None:
    b.relPosNorth += w.relPosNorth*t[1]
    b.relPosEast += w.relPosEast*t[1]
    return

def rotateWaypoint(w, t: tuple) -> None:
    # (N, E)
    permDict = dict({0: (1, 1), 90: (1, -1), 180: (-1, -1), 270: (-1, 1)})
    perm = permDict.get(t[1])
    dir = 1
    if not t[1] == 180 and t[0] == 'L':
        dir = -1

    w.relPosNorth = w.relPosNorth * perm[0] * dir
    w.relPosEast = w.relPosEast * perm[1] * dir
    if t[1] == 90 or t[1] == 270:
        temp = w.relPosNorth
        w.relPosNorth = w.relPosEast
        w.relPosEast = temp
    return


def part1(l: list) -> None:
    ### Part 1 ###
    class Boat:
        def __init__(self, relPosNorth, relPosEast, facingDir):
            super(Boat, self).__init__()
            self.relPosNorth = relPosNorth
            self.relPosEast = relPosEast
            self.facingDir = facingDir

    b = Boat(0, 0, 'E')

    # Loop through instructions #
    for t in l:
        if t[0] == 'N':
            b.relPosNorth += t[1]
        elif t[0] == 'S':
            b.relPosNorth -= t[1]
        elif t[0] == 'E':
            b.relPosEast += t[1]
        elif t[0] == 'W':
            b.relPosEast -= t[1]
        elif t[0] == 'R' or t[0] == 'L':
            updateFacingDir(b, t)
        elif t[0] == 'F':
            moveForward(b, t)
        else:
            print("Unexpected t: (%s, %d)" % (t[0], t[1]))

    # Part 1 answer #
    print("Answer part 1: %d" % (abs(b.relPosNorth) + abs(b.relPosEast)))

def part2(l: list) -> None:
    ### Part 2 ###
    class Boat:
        def __init__(self, relPosNorth, relPosEast):
            super(Boat, self).__init__()
            self.relPosNorth = relPosNorth
            self.relPosEast = relPosEast

    class WayPoint:
        ''' position is relative to the Boat '''
        def __init__(self, relPosNorth, relPosEast):
            super(WayPoint, self).__init__()
            self.relPosNorth = relPosNorth
            self.relPosEast = relPosEast

    b, w = Boat(0, 0), WayPoint(1, 10)

    # Loop through instructions #
    for t in l:
        if t[0] == 'N':
            w.relPosNorth += t[1]
        elif t[0] == 'S':
            w.relPosNorth -= t[1]
        if t[0] == 'E':
            w.relPosEast += t[1]
        elif t[0] == 'W':
            w.relPosEast -= t[1]
        elif t[0] == 'R' or t[0] == 'L':
            rotateWaypoint(w, t)
        elif t[0] == 'F':
            moveBoat(b, w, t)

    # Part 2 answer #
    print("Answer part 2: %d" % (abs(b.relPosNorth) + abs(b.relPosEast)))

def main():

    # Read instructions into a list of tuples #
    l = list()
    with open('input12.txt','r') as f:
        for line in f:
            t = tuple((line[0], int(line[1:].strip('\n'))))
            l.append(t)

    part1(l)
    part2(l)


if __name__ == '__main__':
    main()
