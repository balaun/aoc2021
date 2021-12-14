#advent of code 2021
#day 12
#matt balaun (balaun@gmail.com)

class Cave:
    name=""
    size=0
    connections={}

    def __init__(self, name):
        self.name = name
        if name == name.lower():
            self.size = 0
        else:
            self.size = 1
        self.connections = {}

def print_caves(caves):
    for k in caves.keys():
        print("name: ", caves[k].name, " size: ", caves[k].size, "conn_to: ", ','.join(caves[k].connections.keys()))

def traverse_all_part2(caves):
    retval = set()
    start_cave = caves["start"]
    queue = set()
    for k in start_cave.connections.keys():
        queue.add(("start", "start", k, False))

    while len(queue) > 0:
        dome = queue.pop()
        print(dome)
        currpos = dome[0]
        currpath = dome[1]
        currnext = dome[2]
        currdouble = dome[3]
        
        if currpos == "end": 
            retval.add(currpath)
            print("solution: ", currpath)
        else:
            if currnext == "start":
                continue
            newpos = currnext
            pathtmp = currpath.split(',')
            newpath = list()
            found = False
            for i in range(0, len(pathtmp)):
                if currnext == pathtmp[i]:
                    found = True #path will double back
            pathtmp.append(currnext)
            newpath = ','.join(pathtmp)
            if not found: #no loop to worry about
                for k in caves[newpos].connections.keys():
                    queue.add((newpos, newpath, k, currdouble))
            else: #found == true
                if caves[newpos].size == 0 and currdouble == False:
                    newdouble = True
                    for k in caves[newpos].connections.keys():
                        queue.add((newpos, newpath, k, newdouble))
                else:
                    if caves[newpos].size == 1: #potentially watch out for infinite loop
                        for k in caves[newpos].connections.keys():
                            queue.add((newpos, newpath, k, currdouble))
    return retval


caves={}
data = list()
f = open('input', 'r')
for line in f:
    data.append(line.rstrip())
    tmp = line.rstrip().split('-')
    if tmp[0] not in caves.keys():
        caves[tmp[0]] = Cave(tmp[0])
    if tmp[1] not in caves.keys():
        caves[tmp[1]] = Cave(tmp[1])


    caves[tmp[0]].connections[tmp[1]] = caves[tmp[1]]
    caves[tmp[1]].connections[tmp[0]] = caves[tmp[0]]

print_caves(caves)
paths = traverse_all_part2(caves)
print("part 2: ", len(paths))


