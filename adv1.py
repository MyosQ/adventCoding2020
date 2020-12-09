import os


def main():
    os.chdir("/Users/Frej/Desktop")
    f = open("advCoding/input1.txt", "r");
    numOfRows = len(f.readlines())
    f.seek(0)
    myArr = [0 for j in range(0, numOfRows)]

    i = 0
    for line in f:
        myArr[i] = int(line)
        i += 1

    print(myArr)

    for i in myArr:
        for j in myArr:
            for k in myArr:
                if not (i == j and j == k):
                    if i + j + k == 2020:
                        print(i*j*k)

    f.close()

if __name__ == '__main__':
    main()
