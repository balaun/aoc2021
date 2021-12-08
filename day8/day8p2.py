#aoc2021
#day 8 part 2
#matt balaun (balaun@gmail.com)

#raw_to_siglist
#convert a string to a list of it's component characters
def raw_to_siglist(s):
    retval = list()
    for i in range(0, len(s)):
        retval.append(s[i])
    return retval

#sig_contains takes in two signals, returns True if first contains the second, false otherwise
def sig_contains(s1, s2):
    retval = True
    for s in s2:
        if s not in s1:
            retval = False
    return retval

#takes in two signal lists, returns signals present in first not present in second
def sig_minus(s1, s2):
    retval=list()
    for s in s1:
        if s not in s2:
            retval.append(s)
    return retval

#takes in two signal lists, returns signals present in both
def sig_common(s1, s2):
    retval = list()
    for s in s1:
        if s in s2:
            retval.append(s)
    return retval

#takes in two signal strings, returns true if they are equivalent, false otherwise
def sig_equal(s1, s2):
    ss1 = raw_to_siglist(s1)
    ss2 = raw_to_siglist(s2)
    for i in range(0, len(s1)):
        if ss1[i] not in ss2:
            return False
    for i in range(0, len(s2)):
        if ss2[i] not in ss1:
            return False
    return True

sumnums = 0
data=list()
f = open('input', 'r')
for line in f:
    data.append(line.rstrip())
    sigs10=(line.rstrip().split('|')[0]).rstrip().split(' ')
    print("10sigs: ", sigs10)
    sigs4=(line.rstrip().split('|')[1]).lstrip().split(' ')
    print("4sigs: ", sigs4)

    signals={}
    found0=False
    found1=False
    found2=False
    found3=False
    found4=False
    found5=False
    found6=False
    found7=False
    found8=False
    found9=False
    #begin signal analysis
    for s in sigs10:
        if len(s) == 2:
            #print("found 1")
            found1=True
            signals[1] = s
        if len(s) == 3:
            #print("found 7")
            found7=True
            signals[7] = s
        if len(s) == 4:
            #print("found 4")
            found4=True
            signals[4] = s
        if len(s) == 7:
            #print("found 8")
            found8=True
            signals[8] = s
    for s in sigs4:
        if len(s) == 2:
            #print("found 1")
            found1=True
            signals[1] = s
        if len(s) == 3:
            #print("found 7")
            found7=True
            signals[7] = s
        if len(s) == 4:
            #print("found 4")
            found4=True
            signals[4] = s
        if len(s) == 7:
            #print("found 8")
            found8=True
            signals[8] = s

    #begin deductive phase
    done = False
    nums={}
#    if 8 not in signals.keys():
#        signals[8] = "abcdefg"
    while not done:
        print(signals)
        for i in range(0, len(sigs4)):
            if found1 and found4 and found7 and found8: #we can determine anything else
                if len(sigs4[i]) == 5:
                    #if a 5-piece number contains a 1, then it's a 3
                    if sig_contains(raw_to_siglist(sigs4[i]), raw_to_siglist(signals[1])): #then its a 3
                        #print("found 3")
                        found3 = True
                        signals[3] = sigs4[i]
                    else: #it's a 2 or a 5
                        #if a 5 piece contains a 8-4, it's a 2
                        ptmp = sig_minus(raw_to_siglist(signals[8]), raw_to_siglist(signals[4]))
                        if sig_contains(raw_to_siglist(sigs4[i]), ptmp): #its a 2
                            #print("found2")
                            found2 = True
                            signals[2] = sigs4[i]
                        else: #its a 5
                            #print("found 5")
                            found5 = True
                            signals[5] = sigs4[i]
                if len(sigs4[i]) == 6: #its a 6, 0, or 9
                    if sig_contains(raw_to_siglist(sigs4[i]), raw_to_siglist(signals[4])): #it's a 9
                        found9=True
                        signals[9] = sigs4[i]
                    else:
                        if sig_contains(raw_to_siglist(sigs4[i]), raw_to_siglist(signals[1])): #its a 0
                            found0 = True
                            signals[0] = sigs4[i]
                        else: #its a 6
                            found6 = True
                            signals[6] = sigs4[i]
                    """
                    if sig_contains(raw_to_siglist(sigs4[i]), sig_minus(raw_to_siglist(signals[8]), raw_to_siglist(signals[7]))): #is definitely a 6
                        #print("found6")
                        found6 = True
                        signals[6] = sigs4[i]
                    else: #is a 0 or 9
                        if found6:
                            #if it contains 6-4, it's a 0, else it's a 9
                            ptmp = sig_minus(raw_to_siglist(signals[6]), raw_to_siglist(signals[4]))
                            if sig_contains(raw_to_siglist(sigs4[i]), ptmp):
                                #print("found 0")
                                found0 = True
                                signals[0] = sigs4[i]
                            else:
                                #print("found 9")
                                found9 = True
                                signals[9] = sigs4[i]
                        else: #can't find a 6
                            if found2:
                                ptmp = sig_minus(raw_to_siglist(signals[2]), raw_to_siglist(signals[4]))
                                if sig_contains(raw_to_siglist(sigs4[i]), ptmp): #is a 0
                                    #print("found 0")
                                    found0 = True
                                    signals[0] = sigs4[i]
                                else: #is a 9
                                    #print("found 9")
                                    found9 = True
                                    signals[9] = sigs4[i]
                            else:
                                if found0:
                                    ptmp = sig_minus(raw_to_siglist(signals[0]), raw_to_siglist(signals[4]))
                                    if sig_contains(raw_to_siglist(sigs4[i]), ptmp): #is a 2
                                        #print("found 2")
                                        found2 = True
                                        signals[2] = sigs4[i]
                                    else:
                                        #is a 9
                                        #print("found 9")
                                        found9 = True
                                        signals[9] = sigs4[i]

                                else:
                                    if sig_contains(raw_to_siglist(sigs4[i]), raw_to_siglist(signals[1])):
                                        #is 0 or 9
                                        if sig_contains(raw_to_siglist(sigs4[i]), raw_to_siglist(signals[4])):
                                            #is 9
                                            #print("found 9")
                                            found9 = True
                                            signals[9] = sigs4[i]
                                        else:
                                            #print("found 0")
                                            signals[0] = sigs4[i]
                                            found0 = True
                                    else: #is 6
                                        #print("found 6")
                                        found6 = True
                                        signals[6] = sigs4[i]
                    """

            for i in range(0, len(sigs4)):
                for k in signals.keys():
                    if sig_equal(sigs4[i], signals[k]):
                        nums[i] = k

            if sigs4[i] in signals.values():
#                print("match found")
                for k in signals.keys():
                    if signals[k] == sigs4[i]:
                        nums[i] = k
        if 0 in nums.keys() and 1 in nums.keys() and 2 in nums.keys() and 3 in nums.keys():
            done = True
    print("num found: ", 1000*nums[0] + 100*nums[1] + 10*nums[2] + nums[3])
    sumnums += 1000 * nums[0] + 100 * nums[1] + 10 * nums[2] + nums[3]

print("part 2: ", sumnums)

