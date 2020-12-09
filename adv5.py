import os

def getRow(line):
    Rline = line[0:7]
    Rline = Rline.replace('F', '0')
    Rline = Rline.replace('B', '1')
    rowNr = int(Rline, 2)
    return rowNr

def getCol(line):
    Cline = line[7:]
    Cline = Cline.replace('R', '1')
    Cline = Cline.replace('L', '0')
    colNr = int(Cline, 2)
    return colNr

def getSeatId(r, c):
    return 8*r + c


def main():
    os.chdir("/Users/Frej/Desktop")
    f = open("advCoding/input5.txt", "r");

    # Part 1
    maxSeatId = 0
    for line in f:
        row = getRow(line)
        col = getCol(line)
        seatId = getSeatId(row, col)
        if(seatId > maxSeatId):
            maxSeatId = seatId
    print(maxSeatId)

    # Part 2
    seats = [0 for i in range(0,maxSeatId+1)]
    f.seek(0)
    for line in f:
        row = getRow(line)
        col = getCol(line)
        seatId = getSeatId(row, col)
        seats[seatId] =  1

    emptySeats = [index for index, val in enumerate(seats) if val == 0]
    print(emptySeats)

    f.close()

if __name__ == '__main__':
    main()
