


def trans_Ro(input):
    output = 0
    l = 'IVXLCDM'
    m = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    n = len(input) - 1
    i = 0
    while i <= n:
        if l.index(input[i])%2 == 1:
            if (i+1) > n:
                output += m[input[i]]
                i += 1
                continue
            if m[input[i]] <= m[input[i+1]]:
                print("Hey, ask me something that's not impossible to do!")
                return
            else:
                output += m[input[i]]
                i += 1
        if l.index(input[i])%2 == 0:
            if (i+1) > n:
                output += m[input[i]]
                i += 1
                break
            if m[input[i]] < m[input[i+1]]:
                p = m[input[i+1]] - m[input[i]]
                if (i+2) > n:
                    output += p
                    break
                if p < m[input[i+2]]:
                    print("Hey, ask me something that's not impossible to do!")
                    return
                else:
                    output += p
                    i = i + 2
                    continue
            if m[input[i+1]] == m[input[i]]:
                if (i+2) > n:
                    output += m[input[i]]
                    i += 1
                    continue                
                if m[input[i]] == m[input[i+2]]:                   
                    if m[input[i]] == m[input[i+3]]:
                        print("Hey, ask me something that's not impossible to do!")
                        return
                    else:
                        output += m[input[i]]
                        i += 1
                else:
                    output += m[input[i]]
                    i += 1
            if m[input[i]] > m[input[i+1]]:
                output += m[input[i]]
                i += 1
    print('Sure! It is ' + str(output))
    return

def case_1(input):
    b = input.split()
    b1 = b[2]
    if b1.isdigit():
        if b1[0] == '0':
            print("Hey, ask me something that's not impossible to do!")
            return
        b1 = int(b1)
        if b1 >= 3999:
            print("Hey, ask me something that's not impossible to do!")   
            return
        if (b1 % 1 != 0):
            print("Hey, ask me something that's not impossible to do!")   
            return
        a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        a1 = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        output = ''
        for i, n in enumerate(a):
            while b1 >= a[i]:
                output += a1[i]
                b1 -= a[i]
        print('Sure! It is '+ output)
        return
    if b1.isalpha():
        for char in b1:
            if char not in 'MDCLXVI':
                print("Hey, ask me something that's not impossible to do!")
                return
        if b1 == 'IXI' or b1 =='IXV':
            print("Hey, ask me something that's not impossible to do!")
            return
        trans_Ro(b1)
    else:
        print("Hey, ask me something that's not impossible to do!")
        return
def val_cal(k1, l):
    k = l.index(k1) +1
    if k == 1:
        val =1
        return int(val)
    if (k-1)%2 == 0:
        val =  pow(5, (k-1)/2) * pow(2, (k-1)/2)
        return int(val)
    if (k-1)%2 == 1:
        val = pow(5, k/2) * pow(2, (k-2)/2)
        return int(val)

def ttrans_Ro(input, i2):
    output = 0
    l = i2[::-1]
    for char in input:
        if char not in l:
            print("Hey, ask me something that's not impossible to do!")
            return
    m = {key: val_cal(key, l) for key in l}
    n = len(input) - 1
    i = 0
    while i <= n:
        if l.index(input[i])%2 == 1:
            if (i+1) > n:
                output += m[input[i]]
                i += 1
                continue
            if m[input[i]] <= m[input[i+1]]:
                print("Hey, ask me something that's not impossible to do!")
                return
            else:
                output += m[input[i]]
                i += 1
        if l.index(input[i])%2 == 0:
            if (i+1) > n:
                output += m[input[i]]
                i += 1
                break
            if m[input[i]] < m[input[i+1]]:
                p = m[input[i+1]] - m[input[i]]
                if (i+2) > n:
                    output += p
                    break
                if p < m[input[i+2]]:
                    print("Hey, ask me something that's not impossible to do!")
                    return
                else:
                    output += p
                    i = i + 2
                    continue
            if m[input[i+1]] == m[input[i]]:
                if (i+2) > n:
                    output += m[input[i]]
                    i += 1
                    continue                
                if m[input[i]] == m[input[i+2]]:                   
                    if m[input[i]] == m[input[i+3]]:
                        print("Hey, ask me something that's not impossible to do!")
                        return
                    else:
                        output += m[input[i]]
                        i += 1
                else:
                    output += m[input[i]]
                    i += 1
            if m[input[i]] > m[input[i+1]]:
                output += m[input[i]]
                i += 1
    return output
def case_2(input):
    a = [] 
    b = input[15:]
    b1 = b.split()
    b2 = b1[0] # 转换的对象, 可以为字母或数字
    b4 = b1[1]
    if b4 != 'using':
        print("I don't get what you want, sorry mate!")
        return
    b3 = b1[2] # 必须为字母，为转换的参考值
    if not b3.isalpha():
        print("Hey, ask me something that's not impossible to do!")   
        return
    d2 = str(b2)
    if d2.isdigit():
        c1 = []
        c2 = []
        rb3 = b3[::-1]
        for char in rb3:
            c1.append(char)
        for i,n in enumerate(rb3):
            if i == 0:
                c2.append(rb3[i])
                continue
            if i%2 == 0:
                e = rb3[i-2] + rb3[i]
                c2.append(e)
                c2.append(rb3[i])
            if i%2 == 1:
                e = rb3[i-1] + rb3[i]
                c2.append(e)
                c2.append(rb3[i])
        y = len(rb3)
        a1 = a[-y:]
        rbc2 = c2[::-1]
        output = ''
        b6 = int(b2)
        for i, n in enumerate(a1):
            while b6 >= a1[i]:
                output += rbc2[i]
                b6 -= a1[i]
        print('Sure! It is '+ output)
        return 
    if d2.isalpha():
        output = ttrans_Ro(d2, b3)
        if not output:
            return
        print('Sure! It is ' + str(output))
    return


def case_3a(input): 
    k = input.split()
    k2 = k[2]
    i = k2
    if not k2.isalpha():
        print("Hey, ask me something that's not impossible to do!")
        return
    if len(k2) == 1:
        a = k2[0]
        print("Sure! It is 1 using " + a)
        return
    if len(k2) == 2:
        a = ''.join(k2)
        if k2[0] == k2[1]:
            print("Sure! It is 2 using " + a)
        else: 
            print("Sure! It is 4 using " + a)
        return
    if len(k2) == 3:
        a = ''.join(k2)
        if k2[0] == k2[1] == k2[3]:
            print("Sure! It is 3 using " + a)
        if k2[0] == k2[1] and k2[0] != k2[3]:
            print("Sure! It is 7 using " + a)
        if k2[0] == k2[2] and k2[0] != k2[1]:
            print("Sure! It is 19 using " + a)
        if k2[1] == k2[2] and k2[1] != k2[0]:
            print("Sure! It is 21 using "+ a)
        return
    l = rule_create(input)
    if l == []:
        return
    l1 = ''.join(l)
    l2 = l1[::-1]
    output = ttrans_Ro(i, l2)
    if not output:
        return
    print("Sure! It is " + str(output)+ " using " + str(l2))
    return

def rule_create(input):# by this method you can get the generalized Roman number table
    k = input.split()
    k2 = k[2]
    rev = k2[::-1]
    i = 0
    m = {}
    l = []
    while i < 2:
        a = rev[i]
        if a not in l:
            l.append(a)
        i += 1

    while i <= len(rev) -1:
        a = rev[i]
        b = rev[i-1]
        c = rev[i-2]
        d = rev[i-3]
        if a in l:
            if (a == b or a == b == c) and a != d:
                nb = l.index(b)
                if nb%2 == 1:
                    l.insert(i-1,'_')
                i += 1    
                continue
            if a == c and a != b:
                nc = l.index(c)  
                nb = l.index(b)
                l[nc] = b
                l[nb] = c
                if nb%2 == 1:
                    l.insert(nb, '_')
                if nc%2 == 1:
                    l.insert(nc, '_')
                i += 1
                continue
            if a == d:
                nb = l.index(b)
                nc = l.index(c)
                nd = l.index(d)
                l[nc] = d
                l[nd] = c
                if nc%2 == 1:
                    l.insert(nc, '_')
                if nd%2 == 1:
                    l.insert(nd, '_')                
                if nb%2 == 1:
                    l.insert(nb, '_')
                i += 1
                continue
            else:
                print("Hey, ask me something that's not impossible to do!")
                l = []
                return l
        else:
            l.append(a)
        i += 1
    return l


def please_convert():
    case1 = "Please convert "
    case2 = "using"
    case3 = "minimally"
    i = input('How can I help you? ')
    x = i[:15]  
    z = i.split()
    if x != case1:
        print("I don't get what you want, sorry mate!")
        return 
    if len(z) == 3:
        case_1(i)
        return
    if len(z) == 4 and z[3] == case3:
        case_3a(i)
        return
    if len(z) == 5 and z[3] == case2:
        case_2(i)
        return
    else:
        print("I don't get what you want, sorry mate!")
        return
    # EDIT AND COMPLETE THE CODE ABOVE


# DEFINE OTHER FUNCTIONS

please_convert()
