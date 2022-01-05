# COMP9021 21T3 - Rachid Hamadi
# Quiz 4 *** Due Friday Week 7 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 8 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a strictly positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys



def encode(list_of_integers):
    a = list_of_integers
    k = []
    m = []
    for char in a:
        k.append(bin(char)[2:])
    for char in k:
        q = ''
        for p in str(char):
            q += p + p
        m.append(q)
    output = '0'.join(m)
    output = int(output,2)
    return output
    # REPLACE pass ABOVE WITH YOUR CODE    


def decode(integer):
    p = str(integer)
    p1 = str(bin(integer)[2:])
    n = len(p1)
    i = 0
    l = [] 
    if p == '0' or p == '1' or p == '2':
        return None
    if p == '3':
        return "[1]"
    while i < n :
        a = p1[i]
        b = p1[i+1]
        if n - i == 2:
            if a == b:
                l.append(a)
                break
        c = p1[i+2]
        if n - i == 3:
            if a == 0 and b == c == 1:
                l.append(',')
                l.append('1')
                break
            else:
                return None
        if a == b:
            l.append(a)
            i += 2
            continue
        if a != b:
            if a == 1:
                return None
            if c == 0:
                return None
            else:
                l.append(',')
                i += 1
                continue
    out2 = []
    out1 = ''
    for char in l:
        if char == ',':
            out2.append(int(out1,2))
            out1 =''
            continue
        else:
            out1 += char
    out2.append(int(out1,2))
    return out2
    # REPLACE pass ABOVE WITH YOUR CODE


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))


