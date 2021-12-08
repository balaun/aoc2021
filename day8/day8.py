#advent of code 2021
#day 8
#matt balaun (balaun@gmail.com)


#take in a list of strings, return a list of the individual characters that make up those strings
def find_signal(l):
    retval = list()
    for s in l:
        for i in range(0, len(s)):
            if s[i] not in retval:
                retval.append(s[i])
    return retval

#take in dict of signals, return a deductively reduced dict of those signals
def do_deduction(signals):
    retval = signals
    #first deduction is 7 vs 1
    for c in signals["top"]:
        if (c not in signals["topright"]) and (c not in signals["botright"]): # found top!
            print("found top signal: ", c)
            retval["top"] = list(c)
            for k in retval.keys():
                if c in retval[k]:
                    if k != "top":
                        retval[k].pop(c)
    return retval

#take in two lists of signals, return True if first contains all of the second, false otherwise
def sig_contains(s1, s2):
    retval = True
    for s in s2:
        if s not in s1:
            retval = False
    return retval


data = list()
f = open('input', 'r')
for line in f:
    data.append(line.rstrip())

#for part 1, find 1, 4, 7, or 8 after the vertical pipe
#for part 2, decode all the output values and sum them

ones=0
fours=0
sevens=0
eights=0

for l in data:
    patterns = (l.split('|')[1]).lstrip().split(' ')
#    print(patterns)
    #find candidates for each signal
    top = list()
    topleft = list()
    topright = list()
    mid = list()
    botleft = list()
    botright = list()
    bot = list()
    found1 = False
    found4 = False
    found7 = False
    found8 = False
    p1 = 0
    p4 = 0
    p7 = 0
    p8 = 0
    num1=0
    num2=0
    num3=0
    num4=0
    nums={}
    signals = {}
    for p in patterns:
        if len(p) == 2: #found a 1
            signals[1] = find_signal(list(p))
            found1 = True
            p1 = p
            ones += 1
            if p not in topright:
                topright.append(p)
            if p not in botright:
                botright.append(p)
        if len(p) == 4: #found a 4
            signals[4] = find_signal(list(p))
            found4 = True
            p4 = p
            fours += 1
            if p not in topleft:
                topleft.append(p)
            if p not in topright:
                topright.append(p)
            if p not in mid:
                mid.append(p)
            if p not in botright:
                botright.append(p)
        if len(p) == 3: #found a 7
            signals[7] = find_signal(list(p))
            found7 = True
            p7 = p
            sevens += 1
            if p not in top:
                top.append(p)
            if p not in topright:
                topright.append(p)
            if p not in botright:
                botright.append(p)
        if len(p) == 7: #found a 8
            signals[8] = find_signal(list(p))
            found8 = True
            p8 = p
            eights += 1
            if p not in top:
                top.append(p)
            if p not in topleft:
                topleft.append(p)
            if p not in topright:
                topright.append(p)
            if p not in mid:
                mid.append(p)
            if p not in botleft:
                botleft.append(p)
            if p not in botright:
                botright.append(p)
            if p not in bot:
                bot.append(p)
    """
    if found1 and found7: #then we know the signal for top (0, 2, 3, 5, 6, 9)
        print("found1 and found7")
    if found8 and found7: #then we can identify sixes
        print("found8 and found7")
    if found8 and found4: #then we can identify zero, two or six
        print("found8 and found4")
    if found7 and found4: #then we can identify 5, 6, or 9
        print("found7 and found4")
    if found4 and found1: #then we can identify 5, 6, or 9
        print("found4 and found1")
        # len == 5, is a 5
        # len == 6, has a 1 in it, is a 9
        # len == 6, doesn't have a 1 in it, is a 6
    if found1:
        print("found1")
        #len == 5, has a 1 in it, is a 3
        #len == 5, doesn't have a 1 in it, is a 2 or 5
        #len == 6, has a 1 in it, is a 0 or 9
        #len == 6, doesn't have a 1 in it, is a 6
    if found4 and not found1 and not found7 and not found8:
        print("found4: ", signals[4])
        for i in range(0, len(patterns)):
            ptmp=list()
            for j in range(0, len(patterns[i])):
                ptmp.append(patterns[i][j])
            if len(patterns[i]) == 4:
                nums[i]=4
            if len(patterns[i]) == 5:
                if sig_contains(ptmp, signals[4]): #is invalid
                    print("whoops, invalid signal in found4, len 5, contains 4")
                else:
                    print("number is a 3 or a 5")
            if len(patterns[i]) == 6:
                if sig_contains(ptmp, signals[4]):
                    print("found a 9")
                    signals[9] = ptmp
                    nums[i]=9
                else:
                    print("number is a 0 or a 6")
        #len == 5, has a 4 in it, invalid

        #len == 5, doesn't have a 4 in it. is 3, 5
        #len == 6, has a 4 in it, is a 9
        #len == 6, doesn't have a 4 in it, is 0 or 6
    """

    #now for each segment, find the signal present in every pattern that had it enabled.
    signals["top"] = find_signal(top)
    signals["topleft"] = find_signal(topleft)
    signals["topright"] = find_signal(topright)

    signals["mid"] = find_signal(mid)
    signals["botleft"] = find_signal(botleft)
    signals["botright"] = find_signal(botright)
    signals["bot"] = find_signal(bot)

#    print(signals)
    signals = do_deduction(signals)
#    print(signals)
#    print("\npause\n")
#    c = input()

    """
    if len(p) == 6: #found a 0, 6, or 9
    if len(p) == 5: #found a 2, 3, or 5
    """

print("part 1: ", ones + fours + sevens + eights)

