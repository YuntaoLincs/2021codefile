d1 = {'key3': 4, 'key2': 5, 'key1': 4, 'key4': 2, }
d2 = dict(zip(d1.values(), d1.keys()))
print(d2)


d3 = {'key3': 4, 'key2': 5, 'key1': 4, 'key4': 2, }
d4 = sorted(d1, key=lambda k: d1[k])
print(d4)


my_inverted_dict = dict()
for key, value in d3.items():
    my_inverted_dict.setdefault(value, list()).append(key)

dict = {}


for keys, value in my_inverted_dict.items():
    print(value)
    a = len(value)
    dict[a] = {keys:value}
  
print(dict)

#from collections import defaultdict 
## 翻转的字典 
#reversed_dict = defaultdict(list) 
#for key in keys: 
## 翻转字符串 
#   reversed_dict[mapping[key]].append(key) 
## 如果没有被记录 


print(my_inverted_dict)