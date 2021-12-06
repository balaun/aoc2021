#advent of code 2021
#day 6
#matt balaun (balaun@gmail.com)

class Fish:
    timer=0

    def __init__(self, t):
        self.timer = t


allfish=list()
data = list()
f = open('input', 'r')
for line in f:
    data.append(line.strip())
    for n in line.strip().split(','):
        allfish.append(Fish(int(n)))
            
#begin main simulation loop
day = 0

while (day < 80):
    newfish = list()
    for fish in allfish:
        if fish.timer == 0: #become a 6 and spawn a new fish with an 8
            fish.timer = 6
            newfish.append(Fish(8))
        else:
            fish.timer = fish.timer - 1
    for new in newfish:
        allfish.append(new)
    day += 1

#part 1 answer
print("part1: ", len(allfish))

#need more computationally efficient solution for part 2

allfish = {}
for line in data:
    for n in line.split(','):
        if int(n) in allfish.keys():
            allfish[int(n)] += 1
        else:
            allfish[int(n)] = 1

for i in range(0, 9):
    if i not in allfish.keys():
        allfish[i] = 0

day = 0
while (day < 256):
    newfish = allfish[0]
    allfish[0] = allfish[1]
    allfish[1] = allfish[2]
    allfish[2] = allfish[3]
    allfish[3] = allfish[4]
    allfish[4] = allfish[5]
    allfish[5] = allfish[6]
    allfish[6] = allfish[7] + newfish
    allfish[7] = allfish[8]
    allfish[8] = newfish
    day += 1

sumfish = sum(allfish.values())

#part 2 answer
print("part2: ", sumfish)
