import os

def getLetter(line):
    return(line.split()[1][0])

def getMax(line):
    return(line.split()[0].split("-")[1])

def getMin(line):
    return(line.split()[0].split("-")[0])

def getPwd(line):
    return(line.split()[2])

def getPrev(letter, pwd):
    return pwd.count(letter)

def isValid1(line):
    letter = getLetter(line)
    maxPrev = getMax(line)
    minPrev = getMin(line)
    pwd = getPwd(line)
    prevInPwd = getPrev(letter, pwd)
    if(prevInPwd >= int(minPrev) and prevInPwd <= int(maxPrev)):
        return True
    else:
        return False
def getPos1(line):
    return getMin(line)
def getPos2(line):
    return getMax(line)

def isLetterInPos(letter, pos, pwd):
    #print(letter, pos, pwd)
    if(pwd[int(pos)-1] == letter):
        return True
    else:
        return False

def isValid2(line):
    letter = getLetter(line)
    pos1 = getPos1(line)
    pos2 = getPos2(line)
    pwd = getPwd(line)
    bool1 = isLetterInPos(letter, pos1, pwd)
    bool2 = isLetterInPos(letter, pos2, pwd)

    if(int(bool1)+ int(bool2) == 1):
        return True
    else:
        return False

def main():
    try:
        os.chdir("/Users/Frej/Desktop")
        f = open("input.txt", "r");
    except Exception as e:
        print("hey %s hey" % e)
        raise TypeError("eorrrrror")

    sum1 = 0
    sum2 = 0
    for line in f:
        if(isValid1(line)):
            sum1 += 1
        if(isValid2(line)):
            sum2 += 1;



    print(sum1)
    print(sum2)
    f.close()

if __name__ == '__main__':
    main()
