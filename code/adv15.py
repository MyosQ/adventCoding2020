

def main():

    listSize = 10**2
    with open("input15test.txt", "r") as f:
        arr = [int(i) for i in f.readline().strip().split(',')]

    # init arr #
    ageArr = [-2 for i in range(listSize)]
    for n in arr:
        ageArr[n] = -1

    lastSpoken = arr[-1]

    ind = 4
    while ind < 5:

        if ageArr[lastSpoken] == -1:
            thisSpoken = 0
        elif ageArr[lastSpoken] >= 0:
            thisSpoken = ageArr[lastSpoken]
        else:
            print("HMMM")

        ageArr[thisSpoken] = 0

        print(thisSpoken)
        ageArr[thisSpoken]
        lastSpoken = thisSpoken
        ind += 1

    print(arr)
    print(ageArr)

if __name__ == '__main__':
    main()
