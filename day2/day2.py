#advent of code 2021
#day 2
#Matt Balaun (balaun@gmail.com)

alli=list()
xpos=0
ypos=0
f = open('input', 'r')
for line in f:
    alli.append(line)
    if "up" in line:
        ypos = ypos + int(line.split()[1])
    if "down" in line:
        ypos = ypos - int(line.split()[1])
    if "forward" in line:
        xpos = xpos + int(line.split()[1])

#part 1 answer is final depth * final horizontal position
print(abs(ypos) * xpos)

aim = 0
xpos = 0
ypos = 0
for line in alli:
    if "up" in line:
        aim = aim - int(line.split()[1])
    if "down" in line:
        aim = aim + int(line.split()[1])
    if "forward" in line:
        xpos = xpos + int(line.split()[1])
        ypos = ypos + aim * int(line.split()[1])

#part 2 answer is final xpos * final ypos
print(ypos * xpos)



