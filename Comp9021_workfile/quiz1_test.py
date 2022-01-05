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

# INSERT YOUR CODE HERE
# write two functions, cycles and reversed_dict_per_length.
def f_cycles(small_cycle, n_mapping, key, n_cycles):    
    while True:
        small_cycle.append(key)
        key = n_mapping[key]
        if key not in n_mapping.keys(): 
            return
        if key in small_cycle:
            start = small_cycle.index(key)
            small_cycle = (small_cycle[start:])
            small_cycle = sorted(small_cycle)
            n_cycles.append(small_cycle)
            n_mapping[key] = 0
            return

n_mapping = mapping
n_cycles = []

for key in keys:
    small_cycle = []
    small_cycle.append(key)   
    key = n_mapping[key]
    if key in n_mapping.keys():
        f_cycles(small_cycle, n_mapping, key, cycles)

for i in n_cycles: 
    if not i in cycles:
        cycles.append(i)

cycles = sorted(cycles)

from collections import defaultdict 
 # 翻转的字典 
reversed_dict = defaultdict(list) 
for key in keys: 
 # 翻转字符串 
    reversed_dict[mapping[key]].append(key) 
 # 如果没有被记录 



print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)

