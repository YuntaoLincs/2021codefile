
# COMP9021 21T3
# Quiz 1 *** Due Friday Week 3 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 4 @ 9.00pm
# write two functions, cycles and reversed_dict_per_length.
# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}
key_set = set(keys)

path = []
curr_key = 0
for key in keys:
    curr_key = key
    if curr_key in key_set:
        while True:
            if curr_key in key_set:
                key_set.remove(curr_key)
                path.append(curr_key)
                curr_key = mapping[curr_key]
                if curr_key == key:
                    temp = sorted(path)
                    cycles.append(temp)
                    path = []
                    break
            else:
                break

reversed_dict = {}

for key, value in mapping.items():
    if value not in reversed_dict:
        reversed_dict[value] = [key]
    else:
        reversed_dict[value].append(key)

for key, values in reversed_dict.items():
    
    if len(values) not in reversed_dict_per_length:
        reversed_dict_per_length[len(values)] = {}

reversed_dict_per_length[len(values)][key] = values


print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)