#advent of code 2021
#day5
#matt balaun(balaun@gmail.com)

class Point:
    x=0
    y=0

    def __init__(self):
        self.x=0
        self.y=0

class Line:
    p1=0
    p2=0

    def __init__(self):
        self.p1=Point()
        self.p2=Point()

horizontals=list()
verticals=list()
diagonals=list()
xmax=0
ymax=0
data=list()
f = open('input', 'r')
for line in f:
    data.append(line.strip())
#    print(line.strip())
    stuff=line.strip().split(' ')
    #print(stuff[0])
    #print(stuff[2])
    l = Line()
    l.p1.x=int(stuff[0].split(',')[0])
    l.p1.y=int(stuff[0].split(',')[1])
    l.p2.x=int(stuff[2].split(',')[0])
    l.p2.y=int(stuff[2].split(',')[1])

    if l.p1.x == l.p2.x: #vertical line
        verticals.append(l)
    else:
        if l.p1.y == l.p2.y: #horizontal line
            horizontals.append(l)
        else:
            diagonals.append(l)
    if l.p1.x > xmax:
        xmax = l.p1.x
    if l.p2.x > xmax:
        xmax = l.p2.x
    if l.p1.y > ymax:
        ymax = l.p1.y
    if l.p2.y > ymax:
        ymax = l.p2.y

#print("xmax: ", xmax, " ymax: ", ymax)
#print(len(horizontals), len(verticals), len(diagonals))
mymap = [[0]*1000]*1000
mymap2 = {}
for i in range(0, 1000):
    for j in range(0, 1000):
        mymap2[(i, j)] = 0


for l in horizontals:
    if l.p1.x > l.p2.x:
        t = l.p1.x
        l.p1.x = l.p2.x
        l.p2.x = t
    if l.p1.y != l.p2.y:
        print("whoopsie, screwed up")
        quit()

    for h in range(l.p1.x, l.p2.x + 1):
        mymap[h][l.p2.y] += 1
        mymap2[(h, l.p2.y)] += 1

#print(mymap)

for l in verticals:
    if l.p1.y > l.p2.y:
        t = l.p1.y
        l.p1.y = l.p2.y
        l.p2.y = t
    if l.p1.x != l.p2.x:
        print("whoopsie, screwed up")
        quit()

    for j in range(l.p1.y, l.p2.y + 1):
        mymap[l.p2.x][j] += 1
        mymap2[(l.p2.x, j)] += 1

count = 0
count2 = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        if mymap[i][j] > 1:
            count += 1
        if mymap2[(i, j)] > 1:
            count2 += 1

#print("part 1: ", count) #bizarrely wrong and not sure why
print("part 1: ", count2)

#part 2 begin

for l in diagonals:
    curx = l.p1.x
    cury = l.p1.y
    while curx != l.p2.x and cury != l.p2.y:
        mymap2[(curx, cury)] += 1
        if l.p2.x > curx:
            curx += 1
        else:
            curx = curx - 1
        if l.p2.y > cury:
            cury += 1
        else:
            cury = cury - 1
    mymap2[(curx, cury)] += 1

count2 = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        if mymap2[(i, j)] > 1:
            count2 += 1

print("part 2: ", count2)

