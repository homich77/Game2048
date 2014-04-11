from random import sample
from sql_manager import SqlManager


arrows = {'w': {'step': 1, 'rotate': 1 },
              'a': {'step': 1, 'rotate': 0 },
              's': {'step':-1, 'rotate': 1 },
              'd': {'step':-1, 'rotate': 0 },
              'save': {},
              'exit': {},
              'load': {}
              }

class Struct2048(object):
    # Global variable
    board = []
    isActive = True
    sqlNameKey = 'game2048'

    def __init__(self, size = 4, empty='0'):
        self.size = size
        self.empty = empty
        self.has2048 = False
        self.sql = SqlManager()

    def generate_board(self):
        self.has2048 = False
        self.board = []
        for i in range(self.size):
            self.board.append([self.empty]*self.size)
        self.random_coord(2)

    def random_coord(self,outDigitsCount = 1):
        # Find coordinates of empty fields
        randCoord = tuple([(row,cell) for row in range(self.size) \
                                          for cell in range(self.size) \
                                              if self.board[row][cell] == self.empty])
        if randCoord:
            for x,y in sample(randCoord, outDigitsCount):
                self.board[x][y] = '2'

    def has_empty_field(self):
        for row in self.board:
            for cell in row:
                if cell == self.empty:
                    return True
        print 'Game over'
        return False

    def print_board(self):
        s = ''
        for row in self.board:
            s = ''
            for cell in row:
                s += '{:{width}}'.format(cell, width=5)
            print s
        print ''

    def rotate(self,actionRotate):
        if actionRotate == 1:
            return map(lambda *x:list(x),*self.board)
        else:
            return self.board

    def row_sum(self, row, actionTools):
        tempList = []
        oldValue = self.empty
        for cell in row[::actionTools["step"]]:
            if str(cell) == str(self.empty):
                continue
            elif oldValue == cell:
                tempList.append(str(int(oldValue) * 2))
                oldValue = self.empty
            else:
                if oldValue != self.empty:
                    tempList.append(oldValue)
                oldValue = cell

        if oldValue != self.empty:
            tempList.append(oldValue)
        tempList += [self.empty]*(self.size - len(tempList))
        # Reverse tempList
        return tempList[::actionTools['step']]

    def has_2048(self, row):
        if '2048' in row:
            print "You won!"
            global has2048
            has2048 = True

    def enter_direction(self):
        action = raw_input("Enter direction:")
        if action not in arrows:
            print "It's not correct"
            return self.enter_direction()
        return action

    '''
    def new_board():
        for row in board:
            for cell in row:
                cell = empty
        random_coord(board, 2)'''
    # Game over
    def is_continue(self):
        status = raw_input("Would you like to play again? (y/n):")
        # Start new game
        if status == 'y':
            self.generate_board()
            return True
        # Finish
        else:
            return False



    def move(self, action):
        if action == 'exit':
            self.isActive = False
            return
        elif action == 'save':
            self.sql.set('game2048', self.board)
            return
        elif action == 'load':
            self.board = self.sql.get('game2048')
            if self.board:
                print 'Board was loaded'
                self.isActive = True
            else:
                self.isActive = False
            return

        actionTools = arrows[action]

        oldBoard = list(self.board)
        self.board = self.rotate(actionTools["rotate"])
        for i in range(self.size):
            self.board[i] = self.row_sum(self.board[i], actionTools)
            self.has_2048(self.board[i])
        self.board = self.rotate(actionTools["rotate"])

        hasEmpty = self.has_empty_field()
        if hasEmpty and oldBoard == self.board:
            print 'No move. Please choose another action'
            self.move(self.enter_direction())
        elif oldBoard != self.board and not self.has2048:
            self.random_coord()
            self.isActive = True
        # elif not hasEmpty and not check_sum_opportunity() or has2048:
        elif not hasEmpty or self.has2048:
            self.isActive = self.is_continue()
