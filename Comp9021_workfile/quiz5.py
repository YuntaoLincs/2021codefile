# COMP9021 21T3 - Rachid Hamadi
# Quiz 5 *** Due Friday Week 8 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 8 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines moved to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines moved to the right by one position, e.g.
#      111
#       111
#        111
#         111
# The size is the number of 1s in the parallelogram. In the above examples, the size is 12.

from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


def size_of_largest_parallelogram(matrix):
    stack = []
    size = 0
    row = 0
    col = 0
    for rowh in matrix:
        for colh in rowh:
            size = text(row, col, matrix)
            col += 1
            if size >= 4:
                stack.append(size)
        row += 1 
        col = 0
    if stack == []:
        return 0
    size = max(stack)
    return size 
    # REPLACE PASS ABOVE WITH YOUR CODE
def text(row, col, matrix): 
    t = 0
    stack = []
    n = 0
    c = col
    while(True):
        if c > 9:
            break
        if matrix[row][c] == 0:
            break
        c += 1
        n += 1
    s = left_test(row, col, n, matrix)
    if s >= 4:
        stack.append(s)

    s = rectangle_text(row, col, n, matrix)
    if s >= 4:
        stack.append(s)
    s = right_test(row, col, n, matrix)

    if s >= 4:
        stack.append(s)
    if stack == []: 
        t = 0
        return t
    t = max(stack)
    return t

    
def left_test(row, col, n, matrix): # test the left_parallelogram
    stack = []
    p = 0
    s = 0  # s is the increase time of the row
    while( True):
        if row + 1 > 9:   # prevent the row out of the index
            break
        if matrix[row + 1][col] == 0:
            break
        row += 1
        s += 1
        i = 0
        if col - 1 < 0:
            break
        if matrix[row][col - 1] == 0:
            break
        col -= 1
        c = col
        while(i < n):
            i += 1 
            if c > 8:
                break
            if matrix[row][c+1] == 0:
                n = i
                break
            c += 1 
        p = n * (s+1)
        stack.append(p)
    if stack == []:
        return 0
    p = max(stack)
    return p




def rectangle_text(row, col, n, matrix):
    stack = []
    p = 0
    s = 0  # s is the increase time of the row
    while( True):
        if row + 1 > 9:
            break
        if matrix[row + 1][col] == 0:
            break
        row += 1
        s += 1
        i = 0
        c = col
        while(i < n):
            i += 1 
            if c > 8:
                break
            if matrix[row][c+1] == 0:
                n = i
                break
            c += 1 
        p = i * (s+1)
        stack.append(p)
    if stack == []:
        return 0        
    p = max(stack)
    return p




def right_test(row, col, n, matrix):
    stack = []
    p = 0
    s = 0  # s is the increase time of the row
    while( True):
        if row + 1 > 9:
            break
        if matrix[row + 1][col] == 0:
            break
        row += 1
        s += 1
        i = 0
        if col + 1 > 9:
            break
        if matrix[row][col + 1] == 0:
            break
        col += 1
        c = col
        while(i < n):
            i += 1 
            if c > 8:
                break
            if matrix[row][c+1] == 0:
                n = i
                break
            c += 1 
        p = i * (s+1)
        stack.append(p)
    if stack == []:
        return 0        
    p = max(stack)
    return p
# POSSIBLY DEFINE OTHER FUNCTIONS


try:
    
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram(grid)
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')