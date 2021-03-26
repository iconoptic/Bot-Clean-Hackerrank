#!/usr/bin/python3

# Head ends here
def findDirt(x, y, board, t): #return relative pos of nearest dirt
    curD = []
    for i in range(0, len(board)):
        offset = 0
        while t in board[i][offset:]:
            d = board[i][offset:].index(t)
            if d-x != 0 or i-y != 0: curD.append([offset+d-x,i-y])
            offset = d+offset+1

    for i in curD:
        i.append(abs(i[0])+abs(i[1]))

    curD.sort(key = lambda x: x[2])

    if len(curD) > 0:
        return curD[0][:2]
    else:
        return findDirt(x,y,board,'o')

def mapDirt(curBoard):
    empty = ""
    f = open('map.dat','a+')
    f.close()
    f = open('map.dat','r')
    contents = f.readlines()
    f.close()
    for i in range(0,len(contents)):
        contents[i] = [j for j in contents[i]]
        contents[i].remove('\n')

    if len(contents) < len(curBoard):
        contents = curBoard
    else:
        for i in range(0,len(contents)):
            for j in range(0,len(contents[i])):
                if curBoard[i][j] != contents[i][j] and curBoard[i][j] != 'o':
                    contents[i][j] = curBoard[i][j]

    for i in range(0,len(contents)):
        for j in range(0,len(contents[i])):
            if contents[i][j] == 'b': contents[i][j] == '-'
        contents[i] = empty.join(contents[i])
    for i in range(0,len(contents)):
        contents[i] = empty.join([contents[i],'\n'])

    f = open('map.dat','w')
    f.writelines(contents)
    f.close()

    for i in range(0,len(contents)):
        contents[i] = [j for j in contents[i]]
        contents[i].remove('\n')
    return contents


def next_move(x, y, board):
    if board[x][y] == 'd':
        print("CLEAN")
    else:
        bMap = mapDirt(board)
        target = findDirt(y,x,bMap,'d')
        if target[0] > 0:
            print("RIGHT")
        elif target[0] < 0:
            print("LEFT")
        elif target[1] > 0:
            print("DOWN")
        elif target[1] < 0:
            print("UP")


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
