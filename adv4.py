import os

def getKeyValuePairs(line):
    l = line.split()
    return l;

def addToDict(list, passList, passIndex):
    if(len(passList) <= passIndex):
        passList.append({})
    for l in list:
        splitted = l.split(':')
        key, value = (splitted[0], splitted[1])
        passList[passIndex][key] = value

def addDictToPassList(dict, passList, passIndex):
    passList.append(dict)


def addToDictAtIndex(line, passList, passIndex):
    l = getKeyValuePairs(line)
    addToDict(l, passList, passIndex)

def main():
    os.chdir("/Users/Frej/Desktop")
    f = open("advCoding/input.txt", "r");

    # Read into a list of dictionaries #
    passIndex = 0
    passList = []
    for line in f:
        if(line == '\n'):
            passIndex += 1
        else:
            addToDictAtIndex(line, passList, passIndex)

    # check validity for each pass in passlist #
    nValid = 0
    eyeColors = ['amb', 'blu' ,'brn', 'gry', 'grn', 'hzl', 'oth']
    for d in passList:
        isValid = True
        if(len(d.keys()) == 8 or (len(d.keys()) == 7 and d.get("cid") is None)):
            # Part 1
            #nValid += 1
            #continue

            # Part 2
            if not(len(d.get("byr")) == 4 and int(d.get("byr")) >= 1920 and int(d.get("byr")) <= 2002):
                isValid = False
            if not(len(d.get("byr")) == 4 and int(d.get("iyr")) >= 2010 and int(d.get("iyr")) <= 2020):
                isValid = False
            if not(len(d.get("byr")) == 4 and int(d.get("eyr")) >= 2020 and int(d.get("eyr")) <= 2030):
                isValid = False
            height = d.get("hgt")
            if(height[-2:] == 'cm'):
                height = height[:-2]
                if not(int(height) >= 150 and int(height) <= 193):
                    isValid = False
            elif(height[-2:] == 'in'):
                height = height[:-2]
                if not(int(height) >= 59 and int(height) <= 76):
                    isValid = False
            else:
                isValid = False
            if not(len(d.get("hcl")) == 7 and d.get("hcl")[0] == '#'):
                isValid = False
            elif any(c not in 'abcdef0123456789' for c in d.get("hcl")[1:]):
                isValid = False
            if not(d.get("ecl") in eyeColors):
                isValid = False
            if not(len(d.get("pid")) == 9):
                isValid = False
            elif any(c not in '0123456789' for c in d.get("pid")):
                isValid = False

        else:
            isValid = False


        if(isValid):
            nValid += 1


    print(nValid)
    f.close()

if __name__ == '__main__':
    main()
