from random import sample
import sql_manager

# Global variable
size = 4
empty = '0'
has2048 = False
arrows = {'w': {'step': 1, 'rotate': 1 },
          'a': {'step': 1, 'rotate': 0 },
          's': {'step':-1, 'rotate': 1 },
          'd': {'step':-1, 'rotate': 0 },
          'exit': {}
          }
def generate_board():
    global board
    board = []
    for i in range(size):
        board.append([empty]*size)
    random_coord(2)

def random_coord(outDigitsCount = 1):
    # Find coordinates of empty fields
    randCoord = tuple([(row,cell) for row in range(size) \
                                      for cell in range(size) \
                                          if board[row][cell] == empty])
    if randCoord:
        for x,y in sample(randCoord, outDigitsCount):
            board[x][y] = '2'

def has_empty_field():
    for row in board:
        for cell in row:
            if cell == empty:
                return True
    print 'Game over'
    return False

def print_board():
    for row in board:
        #print "\t".join(row)
        print('{0:{width}}{1:{width}}{2:{width}}{3:{width}}'.format(*row, width=5))
    print ''

def rotate(actionRotate):
    if actionRotate == 1:
        return map(lambda *x:list(x),*board)
    else:
        return board

def row_sum(row, actionTools):
    tempList = []
    oldValue = empty
    for cell in row[::actionTools["step"]]:
        if str(cell) == str(empty):
            continue
        elif oldValue == cell:
            tempList.append(str(int(oldValue) * 2))
            oldValue = empty
        else:
            if oldValue != empty:
                tempList.append(oldValue)
            oldValue = cell

    if oldValue != empty:
        tempList.append(oldValue)
    tempList += [empty]*(size - len(tempList))
    # Reverse tempList
    return tempList[::actionTools['step']]

def has_2048(row):
    if '2048' in row:
        print "You won!"
        global has2048
        has2048 = True

def enter_direction():
    action = raw_input("Enter direction:")
    if action not in arrows:
        print "It's not correct"
        return enter_direction()
    return action

'''
def new_board():
    for row in board:
        for cell in row:
            cell = empty
    random_coord(board, 2)'''
# Game over
def is_continue():
    status = raw_input("Would you like to play again? (y/n):")
    # Start new game
    if status == 'y':
        generate_board()
        return True
    # Finish
    else:
        return False

def move(action):
    if action == 'exit':
        return False

    actionTools = arrows[action]
    global board

    oldBoard = list(board)
    board = rotate(actionTools["rotate"])
    for i in range(size):
        board[i] = row_sum(board[i], actionTools)
        has_2048(board[i])
    board = rotate(actionTools["rotate"])

    hasEmpty = has_empty_field()
    if hasEmpty and oldBoard == board:
        print 'No move. Please choose another action'
        return move(arrows[enter_direction()])
    elif oldBoard != board and not has2048:
        random_coord()
        return True
    # elif not hasEmpty and not check_sum_opportunity() or has2048:
    elif not hasEmpty or has2048:
        return is_continue()
