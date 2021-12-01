#Advent of Code 2021
#day 1
#Matt Balaun (balaun@gmail.com

alllines=list()
f = open('input', 'r')
for line in f:
    alllines.append(line)
up=0
for i in range(0, len(alllines)-1):
    if int(alllines[i]) < int(alllines[i+1]):
        up += 1
#solves part 1
print(up)

up=0
for i in range(0, len(alllines)-3):
    if int(alllines[i]) + int(alllines[i+1]) + int(alllines[i+2]) < int(alllines[i+1]) + int(alllines[i+2]) + int(alllines[i+3]):
        up += 1
#solves part 2
print(up)
