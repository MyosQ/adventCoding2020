import os


def main():
    os.chdir("/Users/Frej/Desktop/advCoding")
    with open("input9test.txt", "r") as f:
        numbers = [int(line.strip('\n')) for line in f]


    dictOfSums = dict()
    preAmbleNum = 5

    # Add all possible sums to boolArr#
    for n in numbers[0:preAmbleNum]:
        for m in numbers[0:preAmbleNum]:
            if not n >= m:
                dictOfSums.update({(n+m): 1})
    print("init ready")
    print(len(dictOfSums))
    print(dictOfSums)
    print(numbers)

    #print(sum(boolArr))

    #for n in range(len(boolArr)):
    #    if boolArr[n]:
    #        print(n)


    indexLowestInPreAmble = 0
    for n in numbers[preAmbleNum: ]:
        sTrue = set()
        for a in numbers[indexLowestInPreAmble:indexLowestInPreAmble+preAmbleNum]:
            for b in numbers[indexLowestInPreAmble:indexLowestInPreAmble+preAmbleNum]:
                if not a == b:
                    sTrue.add(a+b)
        sTest = set()
        for c in dictOfSums.keys():
            sTest.add(c)

        print(numbers[indexLowestInPreAmble:indexLowestInPreAmble+preAmbleNum])
        print(dictOfSums)
        print(sTrue)
        print(sTest)
        print('\n')

        if not (sTest.issubset(sTrue) and sTrue.issubset(sTest)):
            print("something wrong here")
            break

        if not n in dictOfSums.keys():
            print("Not a sum!")
            print(n)
            break

        else:
            #add number#
            for m in numbers[indexLowestInPreAmble+1:indexLowestInPreAmble+preAmbleNum]:
                dictOfSums.update({(n+m): dictOfSums.get(n+m, 0) + 1})

            #remove number#
            for m in numbers[indexLowestInPreAmble+1:indexLowestInPreAmble+preAmbleNum]:
                removeNum = numbers[indexLowestInPreAmble]
                dictOfSums.update({(removeNum+m): dictOfSums.get(removeNum+m)-1})
                if(dictOfSums.get(removeNum+m) == 0):
                    dictOfSums.pop(removeNum+m)


        indexLowestInPreAmble += 1


if __name__ == '__main__':
    main()
