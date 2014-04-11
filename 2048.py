from struct_improved import Struct2048
from optparse import OptionParser

#import argparse

parserO = OptionParser()
parserO.add_option("-l", '--load', dest="load", default='0', help='Load game')
parserO.add_option("-s", '--size', dest="size", type='int', default='4', help='Size board')
parserO.add_option("-e", '--empty', dest="empty", type='str', default='0', help='Value of empty fields')
(options, args) = parserO.parse_args()
'''
parserA = argparse.ArgumentParser()
parserA.add_argument('-n', action='store', dest='n', type='int', help='Simple value n', default='False')
parserA.add_argument('-k', action='store', dest='k', type='int', help='Simple value k', default='True')
'''

game = Struct2048(options.size, options.empty)
print args

if options.load:
    game.board = game.sql.get(game.sqlNameKey)
else:
    game.generate_board()

# isActive = False - "game over"
while game.isActive:
    game.print_board()
    game.move(game.enter_direction())
