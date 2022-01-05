import os
def maze(filename):
    with open(filename) as file_object:
        raw_matrix = file_object.readlines()
        c_p = len(raw_matrix)
        r_p = len(raw_matrix[0].strip())
        for i in raw_matrix:
            i_s = i.strip()
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

def analyse(ma):
    Maz = ma
    if ( Maz == False):
        print('Input does not represent a maze.')
    if ( Maz == None):
        print('Incorrect input.')
    
    gate = get_gate(Maz)
    gatenumber = int(len(gate))
    if gatenumber == 0:
        print('The maze has no gate. ')
    if gatenumber == 1:
        print('The maze has a single gate. ')
    else:
        print('The maze has ' + str(gatenumber) + ' gates')
    return



def is_number(a):  # check input
    if ( a != 0 and a != 1 and a != 2 and a != 3 ):
        return False
    return True 
def get_gate(Maz):
    gate = 0
    ga = []
    for g in Maz[0]:
        if g != 0:
            continue
        i = Maz[0].index(g)
        if ( Maz[0][i-1] == 1 and Maz[0][i+1] == 1 ):
             gate += 1
             ga.append([0,i])
    for g in Maz[-1]:
        if g != 0:
            continue
        i = Maz[-1].index(g)
        if ( Maz[-1][i-1] == 1 and Maz[-1][i+1] == 1 ):
             gate += 1    
             ga.append([0,i])
    n = 0
    g = Maz[n][0]
    ##
    while (g):
        if g != 0:
           continue
        if ( Maz[n-1])
        
    for g in Maz[0]:
        if g != 0:
            continue
        i = Maz[0].index(g)
        if ( Maz[0][i-1] == 1 and Maz[0][i+1] == 1 ):
             gate += 1
             ga.append([0,i])
    for g in Maz[-1]:
        if g != 0:
            continue
        i = Maz[-1].index(g)
        if ( Maz[-1][i-1] == 1 and Maz[-1][i+1] == 1 ):
             gate += 1    
             ga.append([0,i])

    return ga

m = maze('example4.txt')

analyse(m)