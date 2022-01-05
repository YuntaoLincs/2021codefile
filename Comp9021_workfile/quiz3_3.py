import sys


def is_valid(word, arity):
    return False
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')

a1 = arity
w1 = word
alpha_char = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
undercore = '_'
space = ' '
comma = ','
aus = alpha_char + space + undercore
au = alpha_char + undercore
left_par = '('
right_par = ')'
par_map = {')': '('}
other_thing = aus + left_par + right_par + comma

def check_char(string, index1):
    label = True
    count = 0
    for char in string[index1::-1]:  # ), a, 
        if char in aus:
            continue
        if char in au:
            count = count +1
        if char in comma:
            if count == 0:
                label = False
            return label
        if char in left_par:
            label = False
            return label
        if char in right_par:
            return label
    else:
        if count == 0:
            label = False
    return label 

def main(string, a1):
    label = True
    stack = []
    for char in string:
        if char in left_par:
            a_number = 0
            n = a_number
            stack.append(n)
        if char in comma:
            stack[-1] = stack[-1] + 1
            index_1 = string.index(char)
            check_char(string, index_1)
            if label == False:
                return label
        if char in right_par:
            if len(stack) < 1:
                label = False
                return label
            if stack[-1] == a1 - 1:
                stack.pop() 
            else:
                label = False
                return( label )
        if char in aus:
            continue
        if char not in other_thing:
            label = False
            return label
    return label


def is_valid(word, arity):
    label = main( word, arity)
    return label

if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')