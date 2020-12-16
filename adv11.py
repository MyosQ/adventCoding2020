import numpy as np

def part1(arr):
    for round in range(1,100):
        updatedArr = arr.copy()
        for r in range(0, len(arr)):
            for c in range(0, len(arr[0])):
                nOcc = countAdjacentOccupiedSeats(arr, r, c)
                if arr[r][c] == "L":
                    if(nOcc == 0):
                        updatedArr[r][c] = '#'
                elif arr[r][c] == "#":
                    if(nOcc >= 4):
                        updatedArr[r][c] = 'L'

        if((updatedArr == arr).all()):
            print("Steady State!")
            print("Sum: %d" % mySum(arr))
            break
        arr = updatedArr.copy()


def countAdjacentOccupiedSeats(arr, r: int, c: int) -> int:
    h = len(arr)
    w = len(arr[0])
    count = 0
    for rr in range((r-1),(r+1)+1):
        for cc in range((c-1),(c+1)+1):
            if not (rr < 0 or rr >= h or cc < 0 or cc >= w):
                if not(rr == r and cc == c):
                    if arr[rr][cc] == '#':
                        count += 1
    return count

def part2(arr):
    for round in range(0,100):
        updatedArr = arr.copy()
        for r in range(0, len(arr)):
            for c in range(0, len(arr[0])):
                nVisOcc = countVisiblyOccupiedSeats(arr, r, c)
                if arr[r][c] == "L":
                    if(nVisOcc == 0):
                        updatedArr[r][c] = '#'
                elif arr[r][c] == "#":
                    if(nVisOcc >= 5):
                        updatedArr[r][c] = 'L'

        if((updatedArr == arr).all()):
            print("Steady State!")
            print("Sum: %d" % mySum(arr))
            break
        arr = updatedArr.copy()

def countVisiblyOccupiedSeats(arr, r: int, c: int) -> int:
    h = len(arr)
    w = len(arr[0])
    count = 0

    # up #
    occ = False
    for rr in range(r-1, -1, -1):
        if arr[rr][c] == '#':
            occ = True
            break
        elif  arr[rr][c] == 'L':
            occ = False
            break
    if(occ):
        count += 1

    # down #
    occ = False
    for rr in range(r+1, h, 1):
        if arr[rr][c] == '#':
            occ = True
            break
        elif  arr[rr][c] == 'L':
            occ = False
            break
    if(occ):
        count += 1

    # left #
    occ = False
    for cc in range(c-1, -1, -1):
        if arr[r][cc] == '#':
            occ = True
            break
        elif  arr[r][cc] == 'L':
            occ = False
            break
    if(occ):
        count += 1

    # right #
    occ = False
    for cc in range(c+1, w, 1):
        if arr[r][cc] == '#':
            occ = True
            break
        elif  arr[r][cc] == 'L':
            occ = False
            break
    if(occ):
        count += 1

    # up right #
    occ = False
    for cc in range(c+1, w, 1):
        rr = r - abs(cc-c)
        if rr < 0:
            break
        if arr[rr][cc] == '#':
            occ = True
            break
        elif  arr[rr][cc] == 'L':
            occ = False
            break

    if(occ):
        count += 1

    # down right #
    occ = False

    for cc in range(c+1, w, 1):
        rr = r + abs(cc-c)
        if rr >= h:
            break
        if arr[rr][cc] == '#':
            occ = True
            break
        elif  arr[rr][cc] == 'L':
            occ = False
            break

    if(occ):
        count += 1
    # down left #
    occ = False
    for cc in range(c-1, -1, -1):
        rr = r + abs(cc-c)
        if rr >= h:
            break
        if arr[rr][cc] == '#':
            occ = True
            break
        elif  arr[rr][cc] == 'L':
            occ = False
            break
    if(occ):
        count += 1

    # up left #
    occ = False
    for cc in range(c-1, -1, -1):
        rr = r - abs(cc-c)
        if rr < 0:
            break
        if arr[rr][cc] == '#':
            occ = True
            break
        elif  arr[rr][cc] == 'L':
            occ = False
            break
    if(occ):
        count += 1

    return count

def mySum(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if arr[i][j] == '#':
                count += 1

    return count


def main():
    # read file #
    with open("input11.txt", "r") as f:
        lines = list()
        for line in f:
            lines.append(list(line.strip('\n')))

    # read into array #
    arr = np.array(lines)

    # Solving #
    part1(arr)
    part2(arr)

if __name__ == '__main__':
    main()
