
def createDict(line: str) -> dict:
    s = line.strip('\n').split(' ')
    d  = {
        "command": s[0],
        "arg": s[1],
        "isVisited": False
    }
    return d

def exchangeNopToJmp(i: int, dList: list) -> None:
    if(dList[i].get("command") == "jmp"):
        dList[i].update({"command": "nop"})
    elif(dList[i].get("command") == "nop"):
        dList[i].update({"command": "jmp"})

def resetIsVisited(dList: list) -> None:
    for d in dList:
        d.update({"isVisited": False})

def main():
    f = open("/Users/Frej/Desktop/advCoding/input8.txt", "r");

    # Create list
    dList = list()
    for line in f:
        d = createDict(line)
        dList.append(d)

    # Part 1
    if(0):
        sumACC, ind = 0, 0
        while(True):
            d = dList[ind]
            if(d.get("isVisited")):
                break
            if(d.get("command") == "nop"):
                ind += 1
            elif(d.get("command") == "acc"):
                sumACC += int(d.get("arg"))
                ind += 1
            else: #jmp:
                ind += int(d.get("arg"))

            d.update({"isVisited": True})

        print(sumACC)

    # Part 2
    if(1):
        for i in range(0, len(dList)):
            resetIsVisited(dList)
            exchangeNopToJmp(i, dList)
            sumACC, ind = 0, 0
            while(True):
                if(ind == len(dList)):
                    endedNicely = True
                    break
                d = dList[ind]
                if(d.get("isVisited")):
                    endedNicely = False
                    break
                if(d.get("command") == "nop"):
                    ind += 1
                elif(d.get("command") == "acc"):
                    sumACC += int(d.get("arg"))
                    ind += 1
                else: #jmp:
                    ind += int(d.get("arg"))

                d.update({"isVisited": True})

            if(endedNicely):
                break

            exchangeNopToJmp(i, dList)
        print(sumACC)

    f.close()

if __name__ == '__main__':
    main()
