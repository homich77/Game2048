from struct_improved import *

isActive = True
random_coord(2)

# isActive = False - "game over"
while isActive:
    print_board()
    #move(arrows[enter_direction()])
    isActive = move(arrows['a'])
