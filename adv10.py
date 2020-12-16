import os
count = 0

def isValid(nums):
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 3:
            return False
    return True


def removeOneAndTest(nums: list):
    #print(nums)
    global count
    #if isValid(nums):
        #print("Valid")
    count += 1
    #else:
        #print("Not valid")
    #    return

    for i in range(1, (len(nums)-1)):
        #nums.pop(i)
        if(nums[i+1] - nums[i-1] <= 3):
            removeOneAndTest(nums[:i]+nums[i+1:])



def main():
    global count
    os.chdir("/Users/Frej/Desktop/advCoding")
    with open("input10.txt", "r") as f:
        nums = [int(line.strip('\n')) for line in f]

    nums.append(max(nums)+3)
    nums.append(0)
    nums.sort()
    print(nums)

    # Part 1
    sum1, sum2, sum3 = 0, 0, 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            sum1 += 1
        elif nums[i] - nums[i-1] == 2:
            sum2 += 1
        elif nums[i] - nums[i-1] == 3:
            sum3 += 1
        else:
            print(":/")
    #print(sum1, sum2, sum3)
    #print(sum1*sum3)

    # Part 2

    # compulsory adapters
    fixedNums = list()
    fixedNums.append(0)
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1] == 3:
            if not nums[i-1] == fixedNums[-1]:
                fixedNums.append(nums[i-1])
            fixedNums.append(nums[i])
    if not fixedNums[-1] == max(nums):
        fixedNums.append(max(nums))
    print(fixedNums)


    # optional inbetweeners contribution
    prod = 1
    for i in range(1,len(fixedNums)):
        if fixedNums[i] - fixedNums[i-1] <= 3:
            for n in range(fixedNums[i-1]+1, fixedNums[i]):
                if n in nums:
                    prod *= 2
        elif fixedNums[i] - fixedNums[i-1] == 4:
            contrib = 1
            for n in range(fixedNums[i-1]+1, fixedNums[i]):
                if n in nums:
                    contrib *= 2
            contrib -= 1
            prod *= contrib

        else:
            print("----")
            continue
            count = 0
            newList = list()
            for n in range(fixedNums[i-1], fixedNums[i]+1):
                if n in nums:
                    newList.append(n)
            removeOneAndTest(newList)
            prod*= count
            print(count)
            print(newList)


    print(prod)


if __name__ == '__main__':
    main()
