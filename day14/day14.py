#advent of code 2021
#day 14
#matt balaun (balaun@gmail.com)

#apply a single round of polymerization to the input chain
#return the resulting new chain
def apply_polymerization(chain, ops):
    retval = list()

    for i in range(0, len(chain)-1):
        pair = chain[i] + chain[i+1]
        retval.append(chain[i])
        retval.append(ops[pair])
    retval.append(chain[len(chain)-1])
    return retval

#do same thing but more efficiently and with a dict
def apply_2(chaindict, ops):
    retval = {}
    for k in chaindict.keys():
        ins = ops[k]
        pre = k[0]+ins
        post = ins+k[1]

        if pre in retval.keys():
            retval[pre] += chaindict[k]
        else:
            retval[pre] = chaindict[k]

        if post in retval.keys():
            retval[post] += chaindict[k]
        else:
            retval[post] = chaindict[k]
    return retval

def get_mce_count(chain):
    counter = {}
    for i in range(0, len(chain)):
        if chain[i] not in counter.keys():
            counter[chain[i]] = 1
        else:
            counter[chain[i]] += 1
    max_v = max(counter.values())
    #print(counter)
    return max_v 

def get_mce_2(chaindict):
    counter = {}
    for k in chaindict.keys():
        if k[0] in counter.keys():
            counter[k[0]] += chaindict[k]
        else:
            counter[k[0]] = chaindict[k]
        if k[1] in counter.keys():
            counter[k[1]] += chaindict[k]
        else:
            counter[k[1]] = chaindict[k]
    #print(counter)
    retval = max(counter.values())
    if retval % 2 != 0:
        retval = retval - 1
    return retval / 2

def get_lce_count(chain):
    counter = {}
    for i in range(0, len(chain)):
        if chain[i] not in counter.keys():
            counter[chain[i]] = 1
        else:
            counter[chain[i]] += 1
    min_v = min(counter.values())
    #print(counter)
    return min_v

def get_lce_2(chaindict):
    counter = {}
    for k in chaindict.keys():
        if k[0] in counter.keys():
            counter[k[0]] += chaindict[k]
        else:
            counter[k[0]] = chaindict[k]
        if k[1] in counter.keys():
            counter[k[1]] += chaindict[k]
        else:
            counter[k[1]] = chaindict[k]
    #print(counter)
    retval = min(counter.values())
    if retval % 2 != 0:
        retval = retval + 1
    return retval / 2





chain=""
data = list()
ops = {}
f = open('input', 'r')
found = False
for line in f:
    data.append(line.rstrip())
    if line.rstrip() == "":
        found = True
        continue
    if found:
        ops[line.rstrip().split(' ')[0]] = line.rstrip().split(' ')[2] 
    else:
        chain = line.rstrip()

#convert string to list
newchain = list()
for i in range(0, len(chain)):
    newchain.append(chain[i])

chain = newchain

#convert list to dict
chaindict = {}
#print(chain)
for i in range(0, len(chain)-1):
    tmp = chain[i]+chain[i+1]
    #print(tmp)
    if tmp in chaindict.keys():
        chaindict[tmp] += 1
    else:
        chaindict[tmp] = 1


#do the 10 iterations for part 1
for i in range(0, 10):
    #print(chain)
    #print(len(chain))
    #print(chaindict)
    #print(sum(chaindict.values()))
    #c = input("pause")
    chain = apply_polymerization(chain, ops)
    chaindict = apply_2(chaindict, ops)
    

print("part 1: ", get_mce_count(chain)-get_lce_count(chain))
print("part 1 redux: ", get_mce_2(chaindict)-get_lce_2(chaindict))

for i in range(0, 30):
    chaindict = apply_2(chaindict, ops)

print("part 2: ", get_mce_2(chaindict)-get_lce_2(chaindict))

