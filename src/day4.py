import os

def hasWon(board, picked):
    won = False
    unmarkedTotal = 0
    for i in range(len(board)):
        rowComplete = True
        columnComplete = True
        for j in range(len(board[i])):
            # check row
            if board[i][j] not in picked:
                rowComplete = False
                unmarkedTotal += board[i][j]

            # check column 
            # we can do it this way because the length of rows and columns happen to be the same
            # this will not work with non-square boards 
            if board[j][i] not in picked:
                columnComplete = False
        if rowComplete or columnComplete:
            won = True
    
    if won:
        return unmarkedTotal
    else:
        return -1 # board did not win 

# parse input file
file = open(os.path.join(os.path.dirname(__file__), "../data/day4.txt"), 'r')
lines = file.read().splitlines()

picked = [int(i) for i in lines[0].split(',')]
boards = []
board = []

for i in range(2, len(lines)):
    line = lines[i]
    if line == '': # empty line between boards, i.e current board has been finished
        boards.append(board)
        board = []
    else:
        row = [int(i) for i in line.split()]
        board.append(row)

pickedSoFar = []
for num in picked:
    pickedSoFar.append(num)
    for board in boards:
        won = hasWon(board, pickedSoFar)
        if won != -1:
            print(won * num, won, num, board)
            boards.remove(board)