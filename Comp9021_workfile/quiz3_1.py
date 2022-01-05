# 检验字符串中是否为字母，空格，下划线

alpha_char = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
undercore = '_'
space = ' '
comma = ','
aus = alpha_char + space + undercore
au = alpha_char + undercore
left_par = '('
right_par = ')'
par_map = {')': '('}


def par_match(string):
    label = True
    stack = []
    for char in string:
        if char in left_par:
            stack.append(char)
        elif char in right_par:
            if len(stack) < 1:
                label = False
                break
            elif par_map[char] == stack[-1]:
                stack.pop()
            else:
                label = False
                break  
        else:
            continue
    if stack != []:
        label = False
    print(label)
a1 = arity

def main(string):
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
                stack.pop(stack[-1]) 
            else:
                label = False
                return( label )
        if char in aus:
            continue
    return label

def check_char(string, index1):
    label = True
    count = 0
    string1 = reversed(string)
    for char in string1[-index1-1:]:
        if char in aus:
            continue
        if char in au:
            count = count +1
        if char in comma:
            if count == 0:
                label = False
            return label
        if char in left_par:
            if count == 0:
                label = False
            return label
        if char in right_par:
            if count == 0:
                label = False
            return label
    else:
        if count == 0:
            label = False
    return label 
