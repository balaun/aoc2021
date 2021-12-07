#advent of code 2021
#day 7
#matt balaun (balaun@gmail.com)

data = list()
f = open('input', 'r')
for line in f:
    data.append(line.strip())

crabs = list()
for i in data[0].split(','):
    crabs.append(int(i))

crabs.sort()
minfuel = 999999999999999999999
position = 0
for i in range(crabs[0], crabs[len(crabs)-1]):
    fuel = 0
    for j in range(0, len(crabs)):
        fuel += abs(i - crabs[j])
    if fuel <= minfuel:
        minfuel = fuel
        position = i
"""
average = 0
counts = {}
for i in range(0, len(crabs)):
    average += crabs[i]
    if crabs[i] in counts.keys():
        counts[crabs[i]] += 1
    else:
        counts[crabs[i]] = 1
average = average / len(crabs)
maxcount = max(counts.values())
mode = list()
for i in range(0, len(crabs)):
    if counts[crabs[i]] == maxcount:
        mode.append(crabs[i])


print("mean: ", average)
print("median: ", position)
print("mode: ", mode)
"""
print("part 1: ", position)





