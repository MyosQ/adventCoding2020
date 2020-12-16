import os

myList = list()

def addtoExistingSetPart1(line: str, index: int) -> None:
    global myList
    if(len(myList) <= index): # If index is out of range, create new set
        myList.append(set())

    for char in line.strip('\n'):
        myList[index].add(char)

def addtoExistingSetPart2(line: str, index: int) -> None:
    global myList
    if(len(myList) <= index): # If new set, add every letter
        myList.append(set())
        for char in line.strip('\n'):
            myList[index].add(char)

    else: # If existing set, take the intersection
        tempSet = set()
        for char in line.strip('\n'):
            tempSet.add(char)
        myList[index] = myList[index].intersection(tempSet)



def main():
    os.chdir("/Users/Frej/Desktop")
    f = open("advCoding/input6.txt", "r");

    # Add all sets (groups) to a list
    listIndex = 0
    for line in f:
        if(line == '\n'):
            listIndex += 1
            continue
        else:
            addtoExistingSetPart2(line, listIndex)

    print(sum([len(s) for s in myList]))
    f.close()

if __name__ == '__main__':
    main()
