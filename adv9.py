import os

def printArr(myArr, R, C):
    for r in range(0,R):
        for c in range(0,C):
            print(myArr[r][c], end = '')
        print('\n')

def main():
    os.chdir("/Users/Frej/Desktop")
    f = open("grid.txt", "r");
    numOfCols = len(f.readline()) - 1 # -1 for The newline
    f.seek(0)
    numOfRows = len(f.readlines())
    f.seek(0)
    myArr = [[None for i in range(0, numOfCols)] for j in range(0, numOfRows)]



    f.close()

if __name__ == '__main__':
    main()
