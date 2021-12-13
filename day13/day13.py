#advent of code 2021
#day 13
#matt balaun (balaun@gmail.com)


paper={}
data = list()
f = open('input', 'r')
folds = False
for line in f:
    if "fold" in line:
        folds = True
    if not folds and line.rstrip() != "":
        x = int(line.rstrip().split(',')[0])
        y = int(line.rstrip().split(',')[1])
        paper[(x, y)] = '#'
    else:
        if line.rstrip() != "":
            data.append(line.rstrip())

#print(data)
#print(paper)

for fold in data:
    v = fold.split(" ")[2]
    xy = v.split("=")[0]
    val = int(v.split("=")[1])
    print(xy)
    print(val)

    newpaper={}
    if "x" in xy: #vertical line fold
        for p in paper.keys():
            if p[0] > val:
                newpaper[(val-(abs(val-p[0])), p[1])] = '#'
            else:
                newpaper[(p[0], p[1])] = '#'
        paper = newpaper
#        break # only doing 1 fold at first
    if "y" in xy: #horizontal line fold
        for p in paper.keys():
            if p[1] > val:
                newpaper[(p[0], val - (abs(val-p[1])))] = '#'
            else:
                newpaper[(p[0], p[1])] = '#'
        paper = newpaper
#        break # only doing 1 fold at first

xmax = 0
ymax = 0
for p in paper.keys():
    if p[0] > xmax:
        xmax = p[0]
    if p[1] > ymax:
        ymax = p[1]

for j in range(0, ymax+1):
    for i in range(0, xmax+1):
        if (i, j) in paper.keys():
            print("#", end="")
        else:
            print(".", end="")
    print("")

"""

for x in range(0, xmax+1):
    for y in range(0, ymax+1):
        found = False
        for c in range(0, len(paper.keys())):
            if (x, y) == paper.keys()[c]:
                found = True
        if found:
            print("#", end="")
        else:
            print(".", end="")
    print("")

for x in range(0, xmax+1):
    for y in range(0, ymax+1):
        if (x, y) in paper.keys():
            print("#", end="")
        else:
            print(".", end="")
    print("")
"""


#print("part 1:", len(paper))

