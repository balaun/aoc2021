#advent of code 2021
#day 3
#Matt Balaun (balaun@gmail.com)

data=list()
gammarate=0
epsilonrate=0
ones = {}
f = open('input', 'r')
for line in f:
    data.append(line)
    for i in range(0, len(line)):
        if line[i] == "1":
            if i in ones.keys():
                ones[i] = ones[i] + 1
            else:
                ones[i] = 1

for i in range(0, len(data[0])-1):
    gammarate = gammarate * 2
    epsilonrate = epsilonrate * 2
    if i in ones.keys():
        if ones[i] > len(data)/2: #mcb is 1
            gammarate += 1
        else: #mcb is 0
            epsilonrate += 1
    else: #mcb is 0
        epsilonrate += 1


#part 1 answer
print("part 1 gamma: ", gammarate)
print("part 1 epsilon: ", epsilonrate)
print("part 1 answer: ", gammarate * epsilonrate)

#part 2 solution
#from a provided list of bitstrings, bit position, and bit value, return the matching subset of bitstrings
def get_matching_subset(strings, bp, bv):
    retval = list()
    for i in range(0, len(strings)):
        if strings[i][bp] == bv:
            retval.append(strings[i])
    return retval

#from a provided list of bitstrings and bit position, return the most common bit
def get_mcb(strings, bp):
    ones = {}
    for i in range(0, len(strings)):
        for j in range(0, len(strings[0])-1):
            if strings[i][j] == "1":
                if j in ones.keys():
                    ones[j] = ones[j] + 1
                else:
                    ones[j] = 1
    if bp in ones.keys():
        if ones[bp] >= len(strings)/2: #in event of tie, choose the 1
            return "1"
        else:
            return "0"
    else:
        return "0"

#from a provided list of bitstrings and bit position, return the least common bit
def get_lcb(strings, bp):
    zeroes={}
    for i in range(0, len(strings)):
        for j in range(0, len(strings[0])-1):
            if strings[i][j] == "0":
                if j in zeroes.keys():
                    zeroes[j] = zeroes[j] + 1
                else:
                    zeroes[j] = 1
    if bp in zeroes.keys():
        if zeroes[bp] > len(strings)/2: #in event of tie, choose the 1
            return "1"
        else:
            return "0"
    else:
        return "0"

#from a provided bitstring, return the corresponding integer value
def bitstring_to_int(string):
    retval = 0
    for i in range(0, len(string)-1):
        retval = retval * 2
        if string[i] == "1":
            retval += 1
    return retval

oxy=get_matching_subset(data, 0, get_mcb(data, 0))
co2=get_matching_subset(data, 0, get_lcb(data, 0))

i = 0
while len(oxy) > 1:
    i += 1
    oxy=get_matching_subset(oxy, i, get_mcb(oxy, i))

i = 0
while len(co2) > 1:
    i += 1
    co2 = get_matching_subset(co2, i, get_lcb(co2, i))

#part 1 doublecheck
"""
mcbstring = "012345678912\n"
mlist = list(mcbstring)
mlist[0] = get_mcb(data, 0)
mlist[1] = get_mcb(data, 1)
mlist[2] = get_mcb(data, 2)
mlist[3] = get_mcb(data, 3)
mlist[4] = get_mcb(data, 4)
mlist[5] = get_mcb(data, 5)
mlist[6] = get_mcb(data, 6)
mlist[7] = get_mcb(data, 7)
mlist[8] = get_mcb(data, 8)
mlist[9] = get_mcb(data, 9)
mlist[10] = get_mcb(data, 10)
mlist[11] = get_mcb(data, 11)
mcbstring = ''.join(mlist)
print("mcbstring: ", mcbstring)
print("mcb_gamma: ", bitstring_to_int(mcbstring))
print("original gamma: ", gammarate)
lcbstring = "012345678912\n"
llist = list(lcbstring)
llist[0] = get_lcb(data, 0)
llist[1] = get_lcb(data, 1)
llist[2] = get_lcb(data, 2)
llist[3] = get_lcb(data, 3)
llist[4] = get_lcb(data, 4)
llist[5] = get_lcb(data, 5)
llist[6] = get_lcb(data, 6)
llist[7] = get_lcb(data, 7)
llist[8] = get_lcb(data, 8)
llist[9] = get_lcb(data, 9)
llist[10] = get_lcb(data, 10)
llist[11] = get_lcb(data, 11)
lcbstring = ''.join(llist)
print("lcbstring: ", lcbstring)
print("lcb_epsilon: ", bitstring_to_int(lcbstring))
print("original epsilon: ", epsilonrate)
"""

#part 2 answer
print("part 2 answer: ", bitstring_to_int(oxy[0]) * bitstring_to_int(co2[0]))

