#advent of code 2021
#day 4
#matt balaun (balaun@gmail.com)


#return the sum of all unmarked numbers on a board
def get_sum(b):
    retval = 0
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            if b[i][j][1] == False:
                retval += b[i][j][0]
    return retval

#given a called input number, mark that number as called on all the boards
def mark_all(boards, number):
    for b in boards:
        for i in range(0, len(b)):
            for j in range(0, len(b[i])):
                if number == b[i][j][0]:
                    b[i][j] = (number, True)

#check a board to see if it has won
#return 0 if not win
#return positive int score if winner
def check_for_win(b):
    #check rows
    retval = 0
    winner = False
    for i in range(0, len(b)):
        if (b[i][0][1] == True) and (b[i][1][1] == True) and (b[i][2][1] == True) and (b[i][3][1] == True) and (b[i][4][1] == True):
            winner = True
            return get_sum(b)

    #check columns
    retval = 0
    winner = False
    for i in range(0, len(b[0])):
        if (b[0][i][1] == True) and (b[1][i][1] == True) and (b[2][i][1] == True) and (b[3][i][1] == True) and (b[4][i][1] == True):
            winner = True
            return get_sum(b)

    #no winner found, return 0
    if winner == False:
        return 0



f = open('input', 'r')
data = list()

for line in f:
    data.append(line.strip())

draws=list(data[0].split(','))

boards=list()
i = 2
while i < len(data) - 5:
    b = list()
    #print(data[i].split())
    b.append(list(data[i].split()))
    b.append(list(data[i+1].split()))
    b.append(list(data[i+2].split()))
    b.append(list(data[i+3].split()))
    b.append(list(data[i+4].split()))
    boards.append(b)
    i = i + 6

for i in range(0, len(boards)):
    for j in range(0, len(boards[i])):
        for k in range(0, len(boards[i][j])):
            boards[i][j][k] = (int(boards[i][j][k]), False)

#start game loop
i = 0
winner = False
while(i < len(draws) and (len(boards) > 1)):
    #call number
    number = int(draws[i])
    i+=1

    #mark number as called on all boards
    mark_all(boards, number)

    #check all boards for winner
    #and return score of winner
    for b in boards:
        if 0 < check_for_win(b):
            #this was part 1 solution
            if (winner == False):
                print("part 1 winner score: ", number * check_for_win(b))
                winner = True
            #quit()
            boards.remove(b)

if len(boards) == 1:
    while (i < len(draws)):
        number = int(draws[i])
        i+=1

        mark_all(boards, number)

        for b in boards:
            if 0 < check_for_win(b):
                print("part 2 winner: ", number * check_for_win(b))
                quit()




