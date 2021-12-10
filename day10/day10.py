#advent of code 2021
#day 10
#matt balaun (balaun@gmail.com)

#is_corrupted() takes in a line of input
#returns score if line is corrupted
#0 otherwise
def is_corrupted(line):
    stack = list() #expected values
    for c in range(0, len(line)):
        if len(stack) > 0: #then we have to check expected values
            expected = stack[len(stack)-1] #check without popping
            if line[c] == '[':
                stack.append(']')
                continue
            if line[c] == '<':
                stack.append('>')
                continue
            if line[c] == '(':
                stack.append(')')
                continue
            if line[c] == '{':
                stack.append('}')
                continue
            if line[c] == ']' and expected != ']':
                return 57
            if line[c] == ']' and expected == ']':
                stack.pop()
                continue
            if line[c] == '>' and expected != '>':
                return 25137
            if line[c] == '>' and expected == '>':
                stack.pop()
                continue
            if line[c] == ')' and expected != ')':
                return 3
            if line[c] == ')' and expected == ')':
                stack.pop()
                continue
            if line[c] == '}' and expected != '}':
                return 1197
            if line[c] == '}' and expected == '}':
                stack.pop()
                continue
        else: #we just push values
            if line[c] == '[':
                stack.append(']')
                continue
            if line[c] == '<':
                stack.append('>')
                continue
            if line[c] == '(':
                stack.append(')')
                continue
            if line[c] == '{':
                stack.append('}')
                continue
            #invalid character
            print("invalid character found")
            return 0
    if len(stack) == 0:
        print("perfect line found!")
        return 0 #line is not corrupted, and is also not incomplete
    if len(stack) > 1:
        reverse = stack[::-1]
        #print("completion string: ", ''.join(reverse))
        score = 0
        while len(stack) >= 1:
#            print(score)
#            print(stack[len(stack)-1])
            score = score * 5
            if stack[len(stack)-1] == ')':
                score += 1
            if stack[len(stack)-1] == ']':
                score += 2
            if stack[len(stack)-1] == '}':
                score += 3
            if stack[len(stack)-1] == '>':
                score += 4
#            print(score)
            stack.pop()
#        print(score)

#        print("incomplete line")
        return -1 * score

data = list()
f = open('input', 'r')
for line in f:
    data.append(line.rstrip())

total = 0
incompletes = list()
for line in data:
    score = is_corrupted(line)
    if score > 1:
        total += score
    else:
        incompletes.append(line)
print("part1: ", total)

iscores = list()
for line in incompletes:
    iscores.append(-1 * is_corrupted(line))
iscores.sort()
#print(len(iscores))
#print(iscores)
print("part2: ", iscores[len(iscores)//2])
#print("part2: ", iscores[len(iscores)//2 + 1])

