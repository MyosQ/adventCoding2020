def printArr(myArr, R, C):
    for r in range(0,R):
        for c in range(0,C):
            print(myArr[r][c], end = '')
        print('\n')

def main():

    f = open("grid.txt", "r");
    numOfCols = len(f.readline()) - 1 # -1 for The newline
    f.seek(0)
    numOfRows = len(f.readlines())
    f.seek(0)
    myArr = [[None for i in range(0, numOfCols)] for j in range(0, numOfRows)]
    r, c = (0, 0)
    for line in f:
        c = 0
        line = line.strip('\n')
        for symbol in line:
            myArr[r][c] = symbol
            c += 1
        r += 1

    ###########################
    rightSlope, downSlope = (1, 2)
    posRow, posCol = (downSlope,rightSlope)
    numOfTrees = 0
    while(posRow < numOfRows):
        if(myArr[posRow][posCol] == "#"):
            numOfTrees += 1
        posRow += downSlope
        posCol += rightSlope
        posCol %= numOfCols

    print(numOfTrees)

if __name__ == '__main__':
    main()
