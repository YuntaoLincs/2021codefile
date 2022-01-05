
from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def colour_shapes():
    stack_shape = [] # containing the largest shape  
    list = []
    matrip = grid 
    col = 0
    row = 0
    max = 0
    for rowh in matrip:
        for colh in rowh:
            list = BFS(row, col, matrip)     # return a list which contain the path of the largest shape
            col += 1
            if len(list) >= max: 
                max = len(list)
                stack_shape.append(list) 
        row += 1
        col = 0
    nb_of_shapes = stack_shape
    return nb_of_shapes 
    # Replace pass above with your code


def max_number_of_spikes(nb_of_shapes):  # calculate the number of spikes of the largest path
    matrix = grid
    spike = 0
    stack = 0
    for shape in nb_of_shapes:
        for path in shape:
            row = path[0]
            col = path[1]
            n = 0                       # calculate the number of 1s behind
            if row < 9 and matrix[row + 1][col]:       # spike should be the dot which only have one labour of 1s
                n += 1
            if col < 9 and matrix[row][col + 1]:
                n += 1
            if row >= 1 and matrix[row -1][col]:
                n += 1
            if col >= 1 and matrix[row][col - 1]:
                n += 1
            if n == 1:
                spike += 1             
        if spike >= stack:       # compare which path has most spike
            stack = spike
        spike = 0
    return stack
    # Replace pass above with your code

def BFS(row, col, p):
    matri = p
    deque = []   # used by BFS method
    path = [] # record the path of shape, which can be used to calculate the spike
    if matri[row][col]:
        deque.append((row, col))    
    while (deque):
        row = deque[0][0]
        col = deque[0][1]
        matri[row][col] = 3
        path.append((row, col))
        del deque[0]
        c = col 
        if c < 9:
            c += 1
            if matri[row][c] == 1:
                matri[row][c] = 3
                deque.append((row, c))
        r = row
        if r < 9:
            r += 1
            if matri[r][col] == 1:
                matri[r][col] = 3
                deque.append((r, col))
        c = col
        if c >= 1:
            c -= 1
            if matri[row][c] == 1:
                matri[row][c] = 3
                deque.append((row, c))
        r = row
        if r >= 1:
            r -= 1
            if matri[r][col] == 1:
                matri[r][col] = 3
                deque.append((r, col))
    return path
# Possibly define other functions here    


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
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )