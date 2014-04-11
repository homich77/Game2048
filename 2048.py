from struct_improved import size, generate_board, print_board, move
from optparse import OptionParser
#import argparse

parserO = OptionParser()
parserO.add_option("-c", '--continue', dest="iscontinue", type='int', default='0', help='Continue game')
parserO.add_option("-s", '--size', dest="size", type='int', default='4', help='Size board')
parserO.add_option("-n", '--new', dest="new_game", type='int', default='0', help='Start new game')
(options, args) = parserO.parse_args()

if options.size != size:
    size = options.size
print size
generate_board()

print_board()
'''
parserA = argparse.ArgumentParser()
parserA.add_argument('-n', action='store', dest='n', type='int', help='Simple value n', default='False')
parserA.add_argument('-k', action='store', dest='k', type='int', help='Simple value k', default='True')
'''
'''

isActive = True
random_coord(2)

# isActive = False - "game over"
while isActive:
    print_board()
    isActive = move(enter_direction())
    #isActive = move(arrows['a'])


'''
