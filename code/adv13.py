

def part1():
    with open('input13.txt', 'r') as f:
        arrTime = int(f.readline().strip('\n'))
        buses = [int(i) for i in f.readline().split(',') if not i == 'x']

    # Build Sched #
    sched = [0 for i in range(0, arrTime + max(buses))]
    for bus in buses:
        busMultiple = bus
        while busMultiple < (arrTime + bus):
            sched[busMultiple] = bus
            busMultiple += bus

    # Find closest time in schedule #
    for i in range(arrTime, arrTime + min(buses)):
        if not sched[i] == 0:
            busNr = sched[i]
            waitingTime = i - arrTime
            break

    # Part 1 answer #
    print("Part 1 Answer: %d" % (busNr*waitingTime))

def myModInv(p: int, M: int) -> int:
    for i in range(1, M):
        if p*i % M == 1:
            return i
    print("No inverse found")
    return -1

def part2():
    with open('input13test.txt') as f:
        f.readline()
        buses = f.readline().split(',')

    # Read into list of tuples #
    l = list()
    offSet = 0
    for bus in buses:
        if not bus == 'x':
            l.append((int(bus), offSet))
        offSet += 1

    print(l)

    # Get M #
    M = 1
    for t in l:
        M *= t[0]

    # compute x #
    sum = 0
    for t in l:
        print(t)
        m_i = t[0]
        a_i = t[1]
        b_i = int(M/t[0])
        b_i_prim = myModInv(b_i, m_i)#pow(b_i, -1, m_i)
        sum += a_i*b_i*b_i_prim
        #sum %= M

    sum %= M
    x = sum
    print(x)
    print(x % 7)
    print(x % 13)
    print(x % 59)
    print(x % 31)
    print(x % 19)

    print(M)
    print(7*13*59*31*19)
    print(myModInv(2, 7))

def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
