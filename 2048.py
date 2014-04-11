from struct_improved import Struct2048
from optparse import OptionParser
#import argparse

parserO = OptionParser()
parserO.add_option("-c", '--continue', dest="iscontinue", type='int', default='0', help='Continue game')
parserO.add_option("-s", '--size', dest="size", type='int', default='4', help='Size board')
parserO.add_option("-n", '--new', dest="new_game", type='int', default='0', help='Start new game')
parserO.add_option("-e", '--empty', dest="empty", type='str', default='0', help='Value of empty fields')
(options, args) = parserO.parse_args()
'''
parserA = argparse.ArgumentParser()
parserA.add_argument('-n', action='store', dest='n', type='int', help='Simple value n', default='False')
parserA.add_argument('-k', action='store', dest='k', type='int', help='Simple value k', default='True')
'''

game = Struct2048(options.size, options.empty)

game.generate_board()
game.print_board()

'''

isActive = True
random_coord(2)

# isActive = False - "game over"
while isActive:
    print_board()
    isActive = move(enter_direction())
    #isActive = move(arrows['a'])


'''
