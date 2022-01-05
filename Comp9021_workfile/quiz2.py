# COMP9021 21T3 - Rachid Hamadi
# Quiz 2 *** Due Friday Week 4 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 5 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
# 本题的要求是，通过给出的8进制数，输出一个图形
# 解题思路：1. 将8进制数字转换为地图上的坐标
#          2. 将坐标转化为矩阵
#          3. 将矩阵转换为特定图案

# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
# 


class Map:
    def  __init__(self):
        self.On_button = [[0,0]]
        self.position = [0,0]
        self.Xmax = 0
        self.Xmin = 0
        self.Ymax = 0
        self.Ymin = 0
        self.h = 0
        self.w = 0
    def trans_Otal(self, Octal_number): # 此方法可以将8进制数组转换为地图坐标
        for n in Octal_number:
            if (int(n) == 0):                  # 此处目的是根据on_button中最后一个位置来添加新按钮
                x = self.position[0] + 0
                y = self.position[1] + 1              
            elif (int(n) == 1):
                x = self.position[0] + 1
                y = self.position[1] + 1
            elif (int(n) == 2):
                x = self.position[0] + 1
                y = self.position[1] + 0
            elif (int(n) == 3):
                x = self.position[0] + 1
                y = self.position[1] - 1
            elif (int(n) == 4):
                x = self.position[0] + 0
                y = self.position[1] - 1
            elif (int(n) == 5):
                x = self.position[0] - 1
                y = self.position[1] - 1           
            elif (int(n) == 6):
                x = self.position[0] - 1
                y = self.position[1] + 0
            else:
                x = self.position[0] - 1
                y = self.position[1] + 1
            new_point = [x, y]
            self.position = new_point       #报错信息：local variable referenced before assignment--原因一是有全局变量引用未申明，二是变量未赋值被引用
            for i in self.On_button:           # 检验是否有重复项，若有，则删除（可以使用字典来改进遍历方法，提高速度）
                if ( i == new_point):           # 出错原因：修改列表后，循环后， 
                    self.On_button.remove(i)
                    if (x == self.Xmax):
                        self.Xmax = 0
                        for f in self.On_button:
                            if (f[0] >= self.Xmax):
                                self.Xmax = f[0]
                    if (x == self.Xmin):
                        self.Xmin = 0
                        for f in self.On_button:
                            if (f[0] <= self.Xmin):
                                self.Xmin = f[0]
                    if (y == self.Ymax):
                        self.Ymax = 0
                        for f in self.On_button:
                            if (f[0] >= self.Ymax):
                                self.Ymax = f[0]
                    if (y == self.Ymin):
                        self.Ymin = 0
                        for f in self.On_button:
                            if (f[0] <= self.Ymin):
                                self.Ymin = f[0]
                    break
            else:    
                self.On_button.append(new_point) # 添加新位置，并更新xy最大最小值
                if (x  > self.Xmax):
                     self.Xmax = x
                if (x  < self.Xmin):
                     self.Xmin = x
                if (y > self.Ymax):
                     self.Ymax = y
                if (y < self.Ymin):
                     self.Ymin = y
        for m in self.On_button:              #将地图坐标转移至第二象限
            m[0] = m[0] - self.Xmin
            m[1] = m[1] - self.Ymin
        self.h = self.Ymax - self.Ymin           #确定矩阵的长与宽
        self.w = self.Xmax - self.Xmin
    def output_map(self):
        if (self.On_button == []):
            return
        else:    
            w = self.w + 1    
            h = self.h + 1    
            matrix = [[None]*w for i in range(h)]    
            for c in self.On_button:    
                matrix[self.h-c[1]][c[0]] = 1     
            for d in matrix:    
                for e in d:    
                    if (e == 1):    
                        print(on, end="")    
                    else:    
                        print(off, end="")    
                else:    
                    print("") 
        
str_octal = '0'*nb_of_leading_zeroes + f'{int(code):o}' 
list_octal = list(str_octal)[::-1]# 将8进制字符串转换为数组 且反转

new_map = Map()
new_map.trans_Otal(list_octal)

new_map.output_map()