#advent of code 2021
#day 11
#matt balaun (balaun@gmail.com)

"""
#display the grid of octo energy levels only, like in the problem description
def display_octos(octos):
    for i in range(0, len(octos)):
        for j in range(0, len(octos[i])):
            print(octos[i][j][0], end = "")
        print("")

#increment each octo's energy level by 1
#also resets the flashed value to 0
def increment_octos(octos):
    for i in range(0, len(octos)):
        for j in range(0, len(octos[i])):
            if octos[i][j][1] == 1: #apparently if an octo flashed, it can't get any more energy until next turn
                octos[i][j] = (0, 0)
            else:
                e = octos[i][j][0]
                octos[i][j] = (e+1, 0)
    return octos

#handle the flash logic, where each octo with energy > 9 flashes, each flash increases energy of
#adjacent octos (including diagonals) by 1, which can trigger them to flash, each octo can flash only
#once per turn, and each flash resets the octo's energy level to 0
def handle_flashes(octos):
    flashcount = 0
    flasher = True
    while flasher:
        flasher = False
        for i in range(0, len(octos)):
            for j in range(0, len(octos[i])):
                if octos[i][j][0] > 9 and octos[i][j][1] == 0: #octo can flash and hasn't flashed yet
                    flasher = True
                    flashcount += 1
                    octos[i][j] = (0, 1) #FLASH!
                    if i > 0 and i < len(octos)-1 and j > 0 and j < len(octos[i])-1:
                        octos[i+1][j-1] = (octos[i+1][j-1][0]+1, octos[i+1][j-1][1])
                        octos[i+1][j] = (octos[i+1][j][0]+1, octos[i+1][j][1])
                        octos[i+1][j+1] = (octos[i+1][j+1][0]+1, octos[i+1][j+1][1])
                        octos[i][j+1] = (octos[i][j+1][0]+1, octos[i][j+1][1])
                        octos[i][j-1] = (octos[i][j-1][0]+1, octos[i][j-1][1])
                        octos[i-1][j-1] = (octos[i-1][j-1][0]+1, octos[i-1][j-1][1])
                        octos[i-1][j] = (octos[i-1][j][0]+1, octos[i-1][j][1])
                        octos[i-1][j+1] = (octos[i-1][j+1][0]+1, octos[i-1][j+1][1])
                    if i == 0 and j > 0 and j < len(octos[i])-1:
                        octos[i][j-1] = (octos[i][j-1][0]+1, octos[i][j-1][1])
                        octos[i][j+1] = (octos[i][j+1][0]+1, octos[i][j+1][1])
                        octos[i+1][j-1] = (octos[i+1][j-1][0]+1, octos[i+1][j-1][1])
                        octos[i+1][j] = (octos[i+1][j][0]+1, octos[i+1][j][1])
                        octos[i+1][j+1] = (octos[i+1][j+1][0]+1, octos[i+1][j+1][1])
                    if i == len(octos)-1 and j > 0 and j < len(octos[i])-1:
                        octos[i-1][j-1] = (octos[i-1][j-1][0]+1, octos[i-1][j-1][1])
                        octos[i-1][j] = (octos[i-1][j][0]+1, octos[i-1][j][1])
                        octos[i-1][j+1] = (octos[i-1][j+1][0]+1, octos[i-1][j+1][1])
                        octos[i][j-1] = (octos[i][j-1][0]+1, octos[i][j-1][1])
                        octos[i][j+1] = (octos[i][j+1][0]+1, octos[i][j+1][1])
                    if i > 0 and i < len(octos)-1 and j == 0:
                        octos[i-1][j] = (octos[i-1][j][0]+1, octos[i-1][j][1])
                        octos[i-1][j+1] = (octos[i-1][j+1][0]+1, octos[i-1][j+1][1])
                        octos[i][j+1] = (octos[i][j+1][0]+1, octos[i][j+1][1])
                        octos[i+1][j] = (octos[i+1][j][0]+1, octos[i+1][j][1])
                        octos[i+1][j+1] = (octos[i+1][j+1][0]+1, octos[i+1][j+1][1])
                    if i > 0 and i < len(octos)-1 and j == len(octos[i])-1:
                        octos[i-1][j-1] = (octos[i-1][j-1][0]+1, octos[i-1][j-1][1])
                        octos[i-1][j] = (octos[i-1][j][0]+1, octos[i-1][j][1])
                        octos[i][j-1] = (octos[i][j-1][0]+1, octos[i][j-1][1])
                        octos[i+1][j-1] = (octos[i+1][j-1][0]+1, octos[i+1][j-1][1])
                        octos[i+1][j] = (octos[i+1][j][0]+1, octos[i+1][j][1])
                    if i == 0 and j == 0:
                        octos[i+1][j] = (octos[i+1][j][0]+1, octos[i+1][j][1])
                        octos[i][j+1] = (octos[i][j+1][0]+1, octos[i][j+1][1])
                        octos[i+1][j+1] = (octos[i+1][j+1][0]+1, octos[i+1][j+1][1])
                    if i == 0 and j == len(octos[i])-1:
                        octos[i+1][j-1] = (octos[i+1][j-1][0]+1, octos[i+1][j-1][1])
                        octos[i][j-1] = (octos[i][j-1][0]+1, octos[i][j-1][1])
                        octos[i+1][j] = (octos[i+1][j][0]+1, octos[i+1][j][1])
                    if i == len(octos)-1 and j == 0:
                        octos[i-1][j] = (octos[i-1][j][0]+1, octos[i-1][j][1])
                        octos[i-1][j+1] = (octos[i-1][j+1][0]+1, octos[i-1][j+1][1])
                        octos[i][j+1] = (octos[i][j+1][0]+1, octos[i][j+1][1])
                    if i == len(octos)-1 and j == len(octos[i])-1:
                        octos[i-1][j-1] = (octos[i-1][j-1][0]+1, octos[i-1][j-1][1])
                        octos[i][j-1] = (octos[i][j-1][0]+1, octos[i][j-1][1])
                        octos[i-1][j] = (octos[i-1][j][0]+1, octos[i-1][j][1])
    return (octos, flashcount)
"""
def increment_octodict(od):
    retval = od
    for k in retval.keys():
        tmp = retval[k] 
        if tmp[1] == 1:
            retval[k] = (0, 0)
        else:
            retval[k] = (tmp[0]+1, 0)
    return retval

def handle_dict(od):
    retval = od
    flashcount = 0
    flasher = True

    while flasher:
        flasher = False
        for i in range(0, 10):
            for j in range(0, 10):
                tmp = retval[(i, j)]
                if tmp[0] > 9: #flash!
                    flashcount += 1
                    flasher = True
                    retval[(i, j)] = (0, 1)
                    if (i-1, j-1) in retval.keys():
                        retval[(i-1, j-1)] = (retval[(i-1, j-1)][0]+1, retval[(i-1, j-1)][1])
                    if (i, j-1) in retval.keys():
                        retval[(i, j-1)] = (retval[(i, j-1)][0]+1, retval[(i, j-1)][1])
                    if (i+1, j-1) in retval.keys():
                        retval[(i+1, j-1)] = (retval[(i+1, j-1)][0]+1, retval[(i+1, j-1)][1])
                    if (i-1, j) in retval.keys():
                        retval[(i-1, j)] = (retval[(i-1, j)][0]+1, retval[(i-1, j)][1])
                    if (i-1, j+1) in retval.keys():
                        retval[(i-1, j+1)] = (retval[(i-1, j+1)][0]+1, retval[(i-1, j+1)][1])
                    if (i, j+1) in retval.keys():
                        retval[(i, j+1)] = (retval[(i, j+1)][0]+1, retval[(i, j+1)][1])
                    if (i+1, j+1) in retval.keys():
                        retval[(i+1, j+1)] = (retval[(i+1, j+1)][0]+1, retval[(i+1, j+1)][1])
                    if (i+1, j) in retval.keys():
                        retval[(i+1, j)] = (retval[(i+1, j)][0]+1, retval[(i+1, j)][1])
    return (retval, flashcount)


def display_octodict(od):
    for i in range(0, 10):
        for j in range(0, 10):
            if (od[(i, j)][1] == 1):
                print("N", end="")
            else:
                print(od[(i, j)][0], end="")
        print("")

def fix_octodict(od):
    retval = od
    for i in range(0, 10):
        for j in range(0, 10):
            if (retval[(i,j)][1] == 1):
                retval[(i,j)] = (0, 0)
    return retval

octodict={}
x = 0
y = 0
data = list()
octos=list()
f = open('input', 'r')
for line in f:
    octoline = list()
    data.append(line.rstrip())
    y = 0
    for o in range(0, len(line.rstrip())):
        octoline.append((int(line[o]), 0))
        octodict[(x, y)] = (int(line[o]), 0)
        y += 1
    octos.append(octoline)
    x+= 1

step = 0
flashcount = 0
flashcount2 = 0
part1ans = 0
part2ans = 0
while step < 100 or part2ans == 0:
    #print("step: ", step)
    #print("flashcount2: ", flashcount2)
    #display_octos(octos)
    #display_octodict(octodict)
    octodict = fix_octodict(octodict) #fix e = 0 if flashed = 1
    #octos = increment_octos(octos)
    octodict = increment_octodict(octodict)
    #handleme = handle_flashes(octos)
    #octos = handleme[0]
    #flashcount += handleme[1]
    handledict = handle_dict(octodict)
    octodict = handledict[0]
    if step < 100:
        flashcount2 += handledict[1]
        part1ans = flashcount2
    if handledict[1] == 100:
        part2ans = step + 1
    step += 1

#print("part 1: ", flashcount)
print("part 1: ", part1ans)
print("part 2: ", part2ans)

        

