import copy
# 未完成，对定义不清楚

# COMP9021 21T3 - Rachid Hamadi
# Assignment 2 *** Due Monday Week 11 @ 10.00am

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# IMPORT ANY REQUIRED MODULE


class MazeError(Exception):
    def __init__(self, message):
        self.message = message
        print(message)

class Maze:
    def __init__(self, filename):
        self.filename = filename
        # REPLACE PASS ABOVE WITH YOUR CODE
    
    # POSSIBLY DEFINE OTHER METHODS

    def analyse(self):
        Maz = self.op_file(self)
        if ( Maz == False):
            MazeError('Input does not represent a maze.')
        if ( Maz == None):
            MazeError('Incorrect input.')
        
        gate = get_gate(Maz)
        gatenumber = int(len(gate))
        if gatenumber == 0:
            print('The maze has no gate. ')
        if gatenumber == 1:
            print('The maze has a single gate. ')
        else:
            print('The maze has ' + str(gatenumber) + ' gates')

        
        # REPLACE PASS ABOVE WITH YOUR CODE
        
    def display(self):
        pass

    def op_file(self):            # make a matrix full of 0 or 1
        with open(self.filename) as file_object:
            raw_matrix = file_object.readlines()
            c_p = len(raw_matrix)
            r_p = len(raw_matrix[0].strip)
            for i in raw_matrix:
                i_s = i.strip
                k = len(i_s) 
                if ( r_p != k):
                    return None
                if (i_s[-1] == '1' or i_s[-1] == '3'):  # check input
                    return False
            for i in raw_matrix[-1]:
                if ( i == '2' or i == '3'):             # check input
                    return False
        matrix = [[0 for j in range(2*c_p + 1)] for i in range(2*r_p + 1)]
        c = 0
        r = 0
        for row in raw_matrix:
            for col in row:
                if ( col == '\n'):
                    continue
                val = int(col)
                if val == 0:
                    pass
                if val == 1:
                    matrix[r][c] = 1
                    matrix[r][c + 1] = 1
                    matrix[r][c + 2] = 1
                if val == 2:
                    matrix[r][c] = 1
                    matrix[r + 1][c] = 1
                    matrix[r + 2][c] = 1
                if val == 3:
                    matrix[r][c] = 1
                    matrix[r][c + 1] = 1
                    matrix[r][c + 2] = 1
                    matrix[r + 1][c] = 1
                    matrix[r + 2][c] = 1 
                if (is_number(int(col)) == False):
                    return None
                c += 2
            c = 0
            r += 2
        return matrix

def is_number(a):  # check input
    if ( a != 0 and a != 1 and a != 2 and a != 3 ):
        return False
    return True 
        # REPLACE PASS ABOVE WITH YOUR CODE

def get_gate(Maz):
    gate = 0
    ga = []
    for g in Maz[0]:
        if g != 0:
            continue
        i = g.index
        if ( Maz[0][i-1] == 1 and Maz[0][i+1] == 1 ):
             gate += 1
             ga.append([0,i])
    for g in Maz[-1]:
        if g != 0:
            continue
        i = g.index
        if ( Maz[-1][i-1] == 1 and Maz[-1][i+1] == 1 ):
             gate += 1    
             ga.append([0,i])
    trans = [[Maz[j][i] for j in range(len(Maz))] for i in range(len(Maz[0]))]
    for g in trans[0]:
        if g != 0:
            continue
        i = g.index
        if ( trans[0][i-1] == 1 and trans[0][i+1] == 1 ):
             gate += 1
             ga.append([0,i])
    for g in trans[-1]:
        if g != 0:
            continue
        i = g.index
        if ( trans[-1][i-1] == 1 and trans[-1][i+1] == 1 ):
             gate += 1    
             ga.append([0,i])
    return ga
m = Maze('example4.txt')