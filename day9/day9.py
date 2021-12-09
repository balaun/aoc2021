#advent of code 2021
#day 9
#matt balaun (balaun@gmail.com)

# return a set of all points within the basin at the provided starting point
def get_basin(d, p):
    newset = set()
    newset.add(p)
    found = True

    while(found):
        found = False
        for n in newset:
            i = n[0]
            j = n[1]
            if i > 0 and i < len(d)-1 and j > 0 and j < len(d[i])-1: #can go any direction
                if d[i-1][j] < 9 and (i-1, j) not in newset:
                    found = True
                    newset.add((i-1, j))
                    break
                if d[i+1][j] < 9 and (i+1, j) not in newset:
                    found = True
                    newset.add((i+1, j))
                    break
                if d[i][j-1] < 9 and (i, j-1) not in newset:
                    found = True
                    newset.add((i, j-1))
                    break
                if d[i][j+1] < 9 and (i, j+1) not in newset:
                    found = True
                    newset.add((i, j+1))
                    break
            else:
                if i == 0 and j > 0 and j < len(d[i])-1: #can go along j and up i
                    if d[i+1][j] < 9 and (i+1, j) not in newset:
                        found = True
                        newset.add((i+1, j))
                        break
                    if d[i][j-1] < 9 and (i, j-1) not in newset:
                        found = True
                        newset.add((i, j-1))
                        break
                    if d[i][j+1] < 9 and (i, j+1) not in newset:
                        found = True
                        newset.add((i, j+1))
                        break
                else:
                    if i == len(d)-1 and j > 0 and j < len(d[i])-1: #can go along j and down i
                        if d[i-1][j] < 9 and (i-1, j) not in newset:
                            found = True
                            newset.add((i-1, j))
                            break
                        if d[i][j-1] < 9 and (i, j-1) not in newset:
                            found = True
                            newset.add((i, j-1))
                            break
                        if d[i][j+1] < 9 and (i, j+1) not in newset:
                            found = True
                            newset.add((i, j+1))
                            break
                    else:
                        if i > 0 and i < len(d)-1 and j == 0: #can go along i and up j
                            if d[i-1][j] < 9 and (i-1, j) not in newset:
                                found = True
                                newset.add((i-1, j))
                                break
                            if d[i+1][j] < 9 and (i+1, j) not in newset:
                                found = True
                                newset.add((i+1, j))
                                break
                            if d[i][j+1] < 9 and (i, j+1) not in newset:
                                found = True
                                newset.add((i, j+1))
                                break
                        else:
                            if i > 0 and i < len(d)-1 and j == len(d[i])-1: #can go along i and down j
                                if d[i-1][j] < 9 and (i-1, j) not in newset:
                                    found = True
                                    newset.add((i-1, j))
                                    break
                                if d[i+1][j] < 9 and (i+1, j) not in newset:
                                    found = True
                                    newset.add((i+1, j))
                                    break
                                if d[i][j-1] < 9 and (i, j-1) not in newset:
                                    found = True
                                    newset.add((i, j-1))
                                    break
                            else:
                                if i == 0 and j == 0: #can go up i and up j
                                    if d[i+1][j] < 9 and (i+1, j) not in newset:
                                        found = True
                                        newset.add((i+1, j))
                                        break
                                    if d[i][j+1] < 9 and (i, j+1) not in newset:
                                        found = True
                                        newset.add((i, j+1))
                                        break
                                if i == 0 and j == len(d[i]) - 1: #can go up i and down j
                                    if d[i+1][j] < 9 and (i+1, j) not in newset:
                                        found = True
                                        newset.add((i+1, j))
                                        break
                                    if d[i][j-1] < 9 and (i, j-1) not in newset:
                                        found = True
                                        newset.add((i, j-1))
                                        break
                                if i == len(d)-1 and j == 0: #can go down i up j
                                    if d[i-1][j] < 9 and (i-1, j) not in newset:
                                        found = True
                                        newset.add((i-1, j))
                                        break
                                    if d[i][j+1] < 9 and (i, j+1) not in newset:
                                        found = True
                                        newset.add((i, j+1))
                                        break
                                if i == len(d)-1 and j == len(d[i])-1: #can go down i and j, and we're done
                                    if d[i-1][j] < 9 and (i-1, j) not in newset:
                                        found = True
                                        newset.add((i-1, j))
                                        break
                                    if d[i][j-1] < 9 and (i, j-1) not in newset:
                                        found = True
                                        newset.add((i, j-1))
                                        break

    return newset

# solve part 2 with just the data, ignoring lowpoints
def part2_2(d):
    basins = list()
    inabasin=set()

    for i in range(0, len(d)):
        for j in range(0, len(d[i])):
            if d[i][j] < 9 and (i, j) not in inabasin: #new basin detected
                newbasin=get_basin(d, (i,j))
                basins.append(newbasin)
                inabasin.update(newbasin)

    big1 = 0
    big2 = 0
    big3 = 0
    for i in range(0, len(basins)):
        if len(basins[i]) > big1:
            big3 = big2
            big2 = big1
            big1 = len(basins[i])
        else:
            if len(basins[i]) > big2:
                big3 = big2
                big2 = len(basins[i])
            else:
                if len(basins[i]) > big3:
                    big3 = len(basins[i])
    return big1 * big2 * big3
    print("part2: ", big1 * big2 * big3)


# solve part 1 by returning sum of all the lowpoints in the data
def part1(d):
    sum = 0
    lowpoints=list()
    for i in range(0, len(d)):
        for j in range(0, len(d[i])):
            if i > 0 and i < len(d)-1:
                if j > 0 and j < len(d[i])-1:
                    #we're in the middle, compare at will
                    if d[i][j] < d[i][j-1] and d[i][j] < d[i][j+1] and d[i][j] < d[i-1][j] and d[i][j] < d[i+1][j]:
                        #print("found lowpoint: ", d[i][j])
                        lowpoints.append((i,j))
                        sum += d[i][j] + 1
                else: #we're at a j end
                    if j > 0:
                        if d[i][j] < d[i][j-1] and d[i][j] < d[i-1][j] and d[i][j] < d[i+1][j]:
                            #print("found lowpoint: ", d[i][j])
                            lowpoints.append((i,j))
                            sum += d[i][j] + 1
                    if j < len(d[i])-1:
                        if d[i][j] < d[i][j+1] and d[i][j] < d[i-1][j] and d[i][j] < d[i+1][j]:
                            #print("found lowpoint: ", d[i][j])
                            lowpoints.append((i,j))
                            sum += d[i][j] + 1
            else: #we're at a i end
                if i > 0:
                    if j > 0 and j < len(d[i])-1:
                        if d[i][j] < d[i][j-1] and d[i][j] < d[i][j+1] and d[i][j] < d[i-1][j]:
                            #print("found lowpoint: ", d[i][j])
                            lowpoints.append((i,j))
                            sum += d[i][j] + 1
                    else:
                        if j > 0:
                            if d[i][j] < d[i][j-1] and d[i][j] < d[i-1][j]:
                                #print("found lowpoint: ", d[i][j])
                                lowpoints.append((i,j))
                                sum += d[i][j] + 1
                        if j < len(d[i])-1:
                            if d[i][j] < d[i][j+1] and d[i][j] < d[i-1][j]:
                                #print("found lowpoint: ", d[i][j])
                                lowpoints.append((i,j))
                                sum += d[i][j] + 1
                else: 
                    if j > 0 and j < len(d[i])-1:
                        if d[i][j] < d[i][j-1] and d[i][j] < d[i][j+1] and d[i][j] < d[i+1][j]:
                            #print("found lowpoint: ", d[i][j])
                            lowpoints.append((i,j))
                            sum += d[i][j] + 1
                    else:
                        if j > 0:
                            if d[i][j] < d[i][j-1] and d[i][j] < d[i+1][j]:
                                #print("found lowpoint: ", d[i][j])
                                lowpoints.append((i,j))
                                sum += d[i][j] + 1
                        if j < len(d[i])-1:
                            if d[i][j] < d[i][j+1] and d[i][j] < d[i+1][j]:
                                #print("found lowpoint: ", d[i][j])
                                lowpoints.append((i,j))
                                sum += d[i][j] + 1
    return sum

data = list()
f = open('input', 'r')
for line in f:
    tmplist = list()
    tmp = line.rstrip()
    for i in range(0, len(tmp)):
        tmplist.append(int(tmp[i]))
    data.append(tmplist)
#print(data)
print("part 1: ", part1(data))
print("part 2: ", part2_2(data))


