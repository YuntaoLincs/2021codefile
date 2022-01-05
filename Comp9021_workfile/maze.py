# COMP9021 19T3 - Rachid Hamadi
# Assignment 2 *** Due Sunday Week 10
import re
import copy
import os



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
        dic = open_file(self.filename)
        if dic is None:
            MazeError('Incorrect input.')
        elif dic is False:
            MazeError('Input does not represent a maze.')
        else:
            point = green_point(dic)

            
            door = record_door(dic, 0, len(dic) - 1, 0, len(dic[0]) - 1)
            if int(len(door)) == 1:
                print('The maze has a single gate. ')
            elif len(door) == 0:
                print('The maze has no gate. ')
            else:
                print('The maze has ' + str(int(len(door))) + ' gates. ')


            dic1 = copy.deepcopy(dic)
            li = find_walls(dic1, dic)
            if len(li) == 1:
                print('The maze has walls that are all connected. ')
            elif len(li) == 0:
                print('The maze has no wall. ')
            else:
                print('The maze has ' + str(len(li)) + ' sets of walls that are all connected. ')

            li2 = copy.deepcopy(li)
            lii = inner_point(point, dic, li2)
            if len(lii) == 1:
                print('The maze has a unique inaccessible inner point. ')
            elif len(lii) == 0:
                print('The maze has no inaccessible inner point. ')
            else:
                print('The maze has ' + str(len(lii)) + ' inaccessible inner point. ')
                
            dic2 = copy.deepcopy(dic)
            list_cha = cul_de_sacs(dic, li, lii)
            list_cul = correct_cul(dic2, list_cha)
            count_cha_area = count_cha_areas(list_cul, dic)
            dic_area = count_area(dic, door, lii)
            if len(set(dic_area.values())) == 1:
                print('The maze has a unique accessible area. ')
            elif dic_area == {}:
                print('The maze has no accessible area. ')
            else:
                print('The maze has ' + str(len(set(dic_area.values()))) + ' accessible areas. ')

            if len(count_cha_area) == 1:
                print('The maze has accessible cul-de-sacs that are all connected. ')
            elif len(count_cha_area) == 0:
                print('The maze has no accessible cul-de-sac. ')
            else:
                print('The maze has ' + str(len(count_cha_area)) + ' sets of accessible cul-de-sacs that are all '
                                                                   'connected. ')
            dic_path = no_intersection_path(dic, dic_area, list_cul, door, point)
            if len(set(dic_path.values())) == 1:
                print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs. ')
            elif dic_path == {}:
                print('The maze has no entry-exit path with no intersection not to cul-de-sacs. ')
            else:
                print('The maze has ' + str(
                    len(set(dic_path.values()))) + ' entry-exit path with no intersection not to cul-de-sacs. ')

        # REPLACE PASS ABOVE WITH YOUR CODE

    def display(self):
        dic = open_file(self.filename)
        door = record_door(dic, 0, len(dic) - 1, 0, len(dic[0]) - 1)
        point = green_point(dic)
        dic1 = copy.deepcopy(dic)
        li = find_walls(dic1, dic)
        li2 = copy.deepcopy(li)
        lii = inner_point(point, dic, li2)
        list_cha = cul_de_sacs(dic, li, lii)
        dic2 = copy.deepcopy(dic)
        list_cul = correct_cul(dic2, list_cha)
        dic_area = count_area(dic, door, lii)
        dic_path = no_intersection_path(dic, dic_area, list_cul, door, point)
        with open(self.filename.split('.')[0] + '.tex', 'w') as f:
            f.write(r'\documentclass[10pt]{article}' + '\n')
            f.write(r'\usepackage{tikz}' + '\n')
            f.write(r'\usetikzlibrary{shapes.misc}' + '\n')
            f.write(r'\usepackage[margin=0cm]{geometry}' + '\n')
            f.write(r'\pagestyle{empty}' + '\n')
            f.write(r'\tikzstyle{every node}=[cross out, draw, red]' + '\n')
            f.write(r'\begin{document}' + '\n')
            f.write(r'\vspace*{\fill}' + '\n')
            f.write(r'\begin{center}' + '\n')
            f.write(r'\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]' + '\n')
            f.write(r'% Walls' + '\n')
            for i in range(len(li)):
                for j in range(len(li[i])):
                    if (li[i][j][0], li[i][j][1] + 1) in li[i]:
                        f.write(f'    \draw {i, j}  --  {li[i][j][0], li[i][j][1] + 1};\n')
                    if (li[i][j][0], li[i][j][1] - 1) in li[i]:
                        f.write(f'    \draw {i, j}  --  {li[i][j][0], li[i][j][1] - 1} ;\n')
                    if (li[i][j][0] + 1, li[i][j][1]) in li[i]:
                        f.write(f'    \draw {i, j} --  {li[i][j][0] + 1, li[i][j][1]} ;\n')
                    if (li[i][j][0] - 1, li[i][j][1]) in li[i]:
                        f.write(f'    \draw {i, j}  --  {li[i][j][0] - 1, li[i][j][1]} ;\n')
            # f.write(r'% Pillars')
            # f.write(r'')
            f.write(r'\end' + '\n')
            f.write(r'{tikzpicture}' + '\n')
            f.write(r'\end' + '\n')
            f.write(r'{center}' + '\n')
            f.write(r'\vspace * {\fill}' + '\n')
            f.write(r'\end' + '\n')
            f.write(r'{document}' + '\n')

        # os.system("pdflatex maze_2.tex")
        # pdfl = PDFLaTeX.from_texfile('maze_2.tex')
        # pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
        # os.system("pdflatex" + 'maze_2.tex')

#         \fill[green](0, 0) circle(0.2);
#         \fill[green](8, 0)
#         circle(0.2);
#         \fill[green](1, 4)
#         circle(0.2);
#         \fill[green](11, 4)
#         circle(0.2);
#
#     % Inner
#     points in accessible
#     cul - de - sacs
#     \node
#     at(1.5, 0.5)
#     {};
#     \node
#     at(2.5, 0.5)
#     {};
#     \node
#     at(3.5, 0.5)
#     {};
#     \node
#     at(5.5, 0.5)
#     {};
#     \node
#     at(6.5, 0.5)
#     {};
#     \node
#     at(10.5, 0.5)
#     {};
#     \node
#     at(0.5, 1.5)
#     {};
#     \node
#     at(1.5, 1.5)
#     {};
#     \node
#     at(2.5, 1.5)
#     {};
#     \node
#     at(3.5, 1.5)
#     {};
#     \node
#     at(0.5, 2.5)
#     {};
#     \node
#     at(1.5, 2.5)
#     {};
#     \node
#     at(2.5, 2.5)
#     {};
#     \node
#     at(6.5, 2.5)
#     {};
#     \node
#     at(7.5, 2.5)
#     {};
#     \node
#     at(2.5, 3.5)
#     {};
#     \node
#     at(3.5, 3.5)
#     {};
#     \node
#     at(6.5, 3.5)
#     {};
#     \node
#     at(7.5, 3.5)
#     {};
#     \node
#     at(9.5, 3.5)
#     {};
#
# % Entry - exit
# paths
# without
# intersections
# \draw[dashed, yellow](-0.5, 0.5) - - (0.5, 0.5);
# \draw[dashed, yellow](7.5, 0.5) - - (8.5, 0.5);
# \draw[dashed, yellow](0.5, 3.5) - - (1.5, 3.5);
# \draw[dashed, yellow](10.5, 3.5) - - (11.5, 3.5);
# \draw[dashed, yellow](0.5, -0.5) - - (0.5, 0.5);
# \draw[dashed, yellow](0.5, 3.5) - - (0.5, 4.5);
# \draw[dashed, yellow](1.5, 3.5) - - (1.5, 4.5);
# \draw[dashed, yellow](4.5, -0.5) - - (4.5, 4.5);
# \draw[dashed, yellow](7.5, -0.5) - - (7.5, 0.5);
# \draw[dashed, yellow](8.5, -0.5) - - (8.5, 0.5);
# \draw[dashed, yellow](10.5, 3.5) - - (10.5, 4.5);

# REPLACE PASS ABOVE WITH YOUR CODE


# 读取txt文档
def open_file(filename):
    i = 0
    dic = {}
    for line in open(filename):
        if re.fullmatch(r'[ \n]*', line):
            continue
        else:
            dic.update({i: line})
            i += 1
    for j in dic.keys():
        list_num = []
        for k in range(len(dic[j])):
            if re.match('[0-3 \n]', dic[j][k]):
                if re.match('[0-3]', dic[j][k]):
                    list_num.append(dic[j][k])
            else:
                return None
        dic.update({j: list_num})
    if len(dic) < 2 or len(dic) > 41:
        return None
    for p in dic.keys():
        if len(dic[p]) < 2 or len(dic[p]) > 31:
            return None
        if p < len(dic) - 1 and len(dic[p]) != len(dic[p + 1]):
            return None
    for m in dic.keys():
        if dic[m][len(dic[m]) - 1] == '1' or dic[m][len(dic[m]) - 1] == '3':
            return False
    for n in range(len(dic[0])):
        if dic[len(dic) - 1][n] == '2' or dic[len(dic) - 1][n] == '3':
            return False
    return dic


def record_door(dic, im, ii, jm, jj):
    list_door = []
    for i in range(im, ii):
        if dic[i][jm] == '0' or dic[i][jm] == '1':
            if i != ii:
                list_door.append(((2 * i + 1) / 2, jm))
        if dic[i][jj] == '0' or dic[i][jj] == '1':
            if i != ii:
                list_door.append(((2 * i + 1) / 2, jj))
    for j in range(jm, jj):
        if dic[im][j] == '0' or dic[im][j] == '2':
            list_door.append((im, (2 * j + 1) / 2))
        if dic[ii][j] == '0' or dic[ii][j] == '2':
            list_door.append((ii, (2 * j + 1) / 2))
    return list_door


def green_point(dic):
    list_green = []
    if dic[0][0] == '0':
        list_green.append((0, 0))
    for k in range(1, len(dic[0])):
        if dic[0][k] == '0':
            if dic[0][k - 1] == '2' or dic[0][k - 1] == '0':
                list_green.append((0, k))
    for l in range(1, len(dic)):
        if dic[l][0] == '0':
            if dic[l - 1][0] == '1' or dic[l - 1][0] == '0':
                list_green.append((l, 0))
    for i in range(1, len(dic)):
        for j in range(1, len(dic[i])):
            if dic[i][j] == '0':
                if dic[i][j - 1] == '2' or dic[i][j - 1] == '0':
                    if dic[i - 1][j] == '1' or dic[i - 1][j] == '0':
                        list_green.append((i, j))
    return list_green


def check_up(array, dic, li, row, column):
    if array[row][column] != '1' and array[row][column] != '0':
        li.append((row, column))
        array[row][column] = '0'
        if column != 0:
            check_left(array, dic, li, row, column - 1)
        if row != 0:
            check_up(array, dic, li, row - 1, column)
        if column != len(array[0]) - 1 and dic[row][column] == '3':
            check_right(array, dic, li, row, column + 1)


def check_down(array, dic, li, row, column):
    li.append((row, column))
    array[row][column] = '0'
    if column != 0:
        check_left(array, dic, li, row, column - 1)
    if row != len(array) - 1 and dic[row][column] != '1' and dic[row][column] != '0':
        check_down(array, dic, li, row + 1, column)
    if column != len(array[0]) - 1 and dic[row][column] != '2' and dic[row][column] != '0':
        check_right(array, dic, li, row, column + 1)


def check_left(array, dic, li, row, column):
    if array[row][column] != '2' and array[row][column] != '0':
        li.append((row, column))
        array[row][column] = '0'
        if column != 0:
            check_left(array, dic, li, row, column - 1)
        if row != 0:
            check_up(array, dic, li, row - 1, column)
        if row != len(array) - 1 and dic[row][column] == '3':
            check_down(array, dic, li, row + 1, column)


def check_right(array, dic, li, row, column):
    li.append((row, column))
    array[row][column] = '0'
    if column != len(array[0]) - 1 and dic[row][column] != '2' and dic[row][column] != '0':
        check_right(array, dic, li, row, column + 1)
    if row != 0:
        check_up(array, dic, li, row - 1, column)
    if row != len(array) - 1 and dic[row][column] != '1' and dic[row][column] != '0':
        check_down(array, dic, li, row + 1, column)


def find_walls(array, dic):
    li = []
    lii = []
    for j in array.keys():
        for k in range(len(array[j])):
            if array[j][k] != '0':
                array[j][k] = '0'
                li.append((j, k))
                if j != 0:
                    check_up(array, dic, li, j - 1, k)
                if k != 0:
                    check_left(array, dic, li, j, k - 1)
                if j != len(array) - 1 and dic[j][k] != '1':
                    check_down(array, dic, li, j + 1, k)
                if k != len(array[0]) - 1 and dic[j][k] != '2':
                    check_right(array, dic, li, j, k + 1)
                lii.append(li)
                li = []
    return lii


def inner_point(green, dic, li):  # array复制的dic， dic原本的dic， lii墙区域
    key = 0
    inner = []
    for i in range(len(li)):
        centre_point = []
        centre_point2 = []
        dic_cul = {}
        zero_max = []
        one_max = []
        if len(li[i]) != len(set(li[i])):
            li[i] += green
            for j in range(len(li[i])):
                zero_max.append(li[i][j][0])
                one_max.append(li[i][j][1])
            z_max = max(zero_max)
            o_max = max(one_max)
            z_min = min(zero_max)
            o_min = min(one_max)
            part_door = record_door(dic, z_min, z_max, o_min, o_max)
            for j in range(z_min, z_max):
                for k in range(o_min, o_max):
                    centre_point.append(((2 * j + 1) / 2, (2 * k + 1) / 2))
            for j in range(len(li[i])):
                if (li[i][j][0], li[i][j][1]) in li[i] and (li[i][j][0] + 1, li[i][j][1]) in li[i] and (
                        li[i][j][0], li[i][j][1] + 1) in li[i] and (li[i][j][0] + 1, li[i][j][1] + 1) in li[i]:
                    centre_point2.append(((2 * li[i][j][0] + 1) / 2, (2 * li[i][j][1] + 1) / 2))
            for (j, k) in part_door:
                if type(j) == int:
                    if (j + 0.5, k) in centre_point:
                        dic_cul.update({(j + 0.5, k): key})
                        if j + 1.5 < z_max and dic[j + 1][int(k - 0.5)] != '1' and dic[j + 1][int(k - 0.5)] != '3':
                            go_down(centre_point, dic, dic_cul, j + 1.5, k, key, z_min, z_max, o_min, o_max)
                        if k - 1 > o_min and dic[j][int(k - 0.5)] != '2' and dic[j][int(k - 0.5)] != '3':
                            go_left(centre_point, dic, dic_cul, j + 0.5, k - 1, key, z_min, z_max, o_min, o_max)
                        if k + 1 < o_max and dic[j][int(k + 0.5)] != '2' and dic[j][int(k + 0.5)] != '3':
                            go_right(centre_point, dic, dic_cul, j + 0.5, k + 1, key, z_min, z_max, o_min, o_max)
                    elif (j - 0.5, k) in centre_point:
                        dic_cul.update({(j - 0.5, k): key})
                        if j - 1.5 > z_min and dic[j - 1][int(k - 0.5)] != '1' and dic[j - 1][int(k - 0.5)] != '3':
                            go_up(centre_point, dic, dic_cul, j - 1.5, k, key, z_min, z_max, o_min, o_max)
                        if k - 1 > o_min and dic[j - 1][int(k - 0.5)] != '2' and dic[j - 1][int(k - 0.5)] != '3':
                            go_left(centre_point, dic, dic_cul, j - 0.5, k - 1, key, z_min, z_max, o_min, o_max)
                        if k + 1 < o_max and dic[j - 1][int(k + 0.5)] != '1' and dic[j - 1][int(k + 0.5)] != '3':
                            go_right(centre_point, dic, dic_cul, j - 0.5, k + 1, key, z_min, z_max, o_min, o_max)
                else:
                    if (j, k + 0.5) in centre_point:
                        dic_cul.update({(j, k + 0.5): key})
                        if j - 1 > z_min and dic[int(j - 0.5)][k] != '1' and dic[int(j - 0.5)][k] != '3':
                            go_up(centre_point, dic, dic_cul, j - 1, k + 0.5, key, z_min, z_max, o_min, o_max)
                        if j + 1 < z_max + 1 and dic[int(j + 0.5)][k] != '1' and dic[int(j + 0.5)][k] != '3':
                            go_down(centre_point, dic, dic_cul, j + 1, k + 0.5, key, z_min, z_max, o_min, o_max)
                        if k + 1.5 < o_max and dic[int(j - 0.5)][k + 1] != '2' and dic[int(j - 0.5)][k + 1] != '3':
                            go_right(centre_point, dic, dic_cul, j, k + 1.5, key, z_min, z_max, o_min, o_max)
                    elif (j, k - 0.5) in centre_point:
                        dic_cul.update({(j, k - 0.5): key})
                        if j - 1 > z_min and dic[int(j - 0.5)][k - 1] != '1' and dic[int(j - 0.5)][k - 1] != '3':
                            go_up(centre_point, dic, dic_cul, j - 1, k + 0.5, key, z_min, z_max, o_min, o_max)
                        if j + 1 < z_max and dic[int(j + 0.5)][k - 1] != '1' and dic[int(j + 0.5)][k - 1] != '3':
                            go_down(centre_point, dic, dic_cul, j + 1, k - 0.5, key, z_min, z_max, o_min, o_max)
                        if k - 1.5 > o_min and dic[int(j - 0.5)][k - 1] != '2' and dic[int(j - 0.5)][k - 1] != '3':
                            go_left(centre_point, dic, dic_cul, j, k - 1.5, key, z_min, z_max, o_min, o_max)
                key += 1
            inner += list(set(centre_point).difference(set(dic_cul.keys())).intersection(set(centre_point2)))
    inner = list(set(inner))
    return inner


def go_up(liii, dic, areas, i, j, count, z_min, z_max, o_min, o_max):
    if (i, j) not in areas.keys():
        areas.update({(i, j): count})
        if i - 1 > z_min and (i - 1, j) in liii:
            if dic[int(i - 0.5)][int(j - 0.5)] != '1' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                go_up(liii, dic, areas, i - 1, j, count, z_min, z_max, o_min, o_max)
        if j - 1 > o_min and (i, j - 1) in liii:
            if dic[int(i - 0.5)][int(j - 0.5)] != '2' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                go_left(liii, dic, areas, i, j - 1, count, z_min, z_max, o_min, o_max)
        if j + 1 < o_max and (i, j + 1) in liii:
            if dic[int(i - 0.5)][int(j + 0.5)] != '2' and dic[int(i - 0.5)][int(j + 0.5)] != '3':
                go_right(liii, dic, areas, i, j + 1, count, z_min, z_max, o_min, o_max)


def go_down(liii, dic, areas, i, j, count, z_min, z_max, o_min, o_max):
    if (i, j) not in areas.keys():
        areas.update({(i, j): count})
        if i + 1 < z_max and (i + 1, j) in liii:
            if dic[int(i + 0.5)][int(j - 0.5)] != '1' and dic[int(i + 0.5)][int(j - 0.5)] != '3':
                go_down(liii, dic, areas, i + 1, j, count, z_min, z_max, o_min, o_max)
        if j - 1 > o_min and (i, j - 1) in liii:
            if dic[int(i - 0.5)][int(j - 0.5)] != '2' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                go_left(liii, dic, areas, i, j - 1, count, z_min, z_max, o_min, o_max)
        if j + 1 < o_max and (i, j + 1) in liii:
            if dic[int(i - 0.5)][int(j + 0.5)] != '2' and dic[int(i - 0.5)][int(j + 0.5)] != '3':
                go_right(liii, dic, areas, i, j + 1, count, z_min, z_max, o_min, o_max)


def go_left(liii, dic, areas, i, j, count, z_min, z_max, o_min, o_max):
    if (i, j) not in areas.keys():
        areas.update({(i, j): count})
        if i - 1 > z_min and (i - 1, j) in liii:
            if dic[int(i - 0.5)][int(j - 0.5)] != '1' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                go_up(liii, dic, areas, i - 1, j, count, z_min, z_max, o_min, o_max)
        if i + 1 < z_max and (i + 1, j) in liii:
            if dic[int(i + 0.5)][int(j - 0.5)] != '1' and dic[int(i + 0.5)][int(j - 0.5)] != '3':
                go_down(liii, dic, areas, i + 1, j, count, z_min, z_max, o_min, o_max)
        if j - 1 > o_min and (i, j - 1) in liii:
            if dic[int(i - 0.5)][int(j - 0.5)] != '2' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                go_left(liii, dic, areas, i, j - 1, count, z_min, z_max, o_min, o_max)


def go_right(liii, dic, areas, i, j, count, z_min, z_max, o_min, o_max):
    if (i, j) not in areas.keys():
        areas.update({(i, j): count})
        if i - 1 > z_min and (i - 1, j) in liii:
            if dic[int(i - 0.5)][int(j - 0.5)] != '1' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                go_up(liii, dic, areas, i - 1, j, count, z_min, z_max, o_min, o_max)
        if i + 1 < z_max and (i + 1, j) in liii:
            if dic[int(i + 0.5)][int(j - 0.5)] != '1' and dic[int(i + 0.5)][int(j - 0.5)] != '3':
                go_down(liii, dic, areas, i + 1, j, count, z_min, z_max, o_min, o_max)
        if j + 1 < o_max and (i, j + 1) in liii:
            if dic[int(i - 0.5)][int(j + 0.5)] != '2' and dic[int(i - 0.5)][int(j + 0.5)] != '3':
                go_right(liii, dic, areas, i, j + 1, count, z_min, z_max, o_min, o_max)


def count_area(dic, door, lii):
    liii = []
    for i in range(len(dic) - 1):
        for j in range(len(dic[0]) - 1):
            liii.append((i + 0.5, j + 0.5))
    liii = list(set(liii).difference(set(lii)))
    areas = {}
    count = 0
    if len(door) == 0:
        return {}
    else:
        for (i, j) in liii:
            if (i, j) not in areas.keys():
                areas.update({(i, j): count})
                if i - 1 > 0 and (i - 1, j) in liii:
                    if dic[int(i - 0.5)][int(j - 0.5)] != '1' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                        go_up(liii, dic, areas, i - 1, j, count, 0, len(dic), 0, len(dic[0]))
                if i + 1 < len(dic) and (i + 1, j) in liii:
                    if dic[int(i + 0.5)][int(j - 0.5)] != '1' and dic[int(i + 0.5)][int(j - 0.5)] != '3':
                        go_down(liii, dic, areas, i + 1, j, count, 0, len(dic), 0, len(dic[0]))
                if j - 1 > 0 and (i, j - 1) in liii:
                    if dic[int(i - 0.5)][int(j - 0.5)] != '2' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                        go_left(liii, dic, areas, i, j - 1, count, 0, len(dic), 0, len(dic[0]))
                if j + 1 < len(dic[0]) and (i, j + 1) in liii:
                    if dic[int(i - 0.5)][int(j + 0.5)] != '2' and dic[int(i - 0.5)][int(j + 0.5)] != '3':
                        go_right(liii, dic, areas, i, j + 1, count, 0, len(dic), 0, len(dic[0]))
                count += 1
    return areas


def cul_de_sacs(dic, li, li2):
    lii = []
    for i in range(len(li)):
        for (j, k) in li[i]:
            if (j, k + 1) in li[i] and (j + 1, k) in li[i] and (j + 1, k + 1) in li[i]:
                if ((2 * j + 1) / 2, (2 * k + 1) / 2) not in li2:
                    lii.append(((2 * j + 1) / 2, (2 * k + 1) / 2))
    for i in range(len(lii) - 1):
        count = 0
        if dic[int(lii[i][0] - 0.5)][int(lii[i][1] - 0.5)] != '3' and dic[int(lii[i][0] - 0.5)][
            int(lii[i][1] - 0.5)] != '1' and (lii[i][0] - 1, lii[i][1]) not in lii:
            count += 1
        if dic[int(lii[i][0] - 0.5)][int(lii[i][1] - 0.5)] != '3' and dic[int(lii[i][0] - 0.5)][
            int(lii[i][1] - 0.5)] != '2' and (lii[i][0], lii[i][1] - 1) not in lii:
            count += 1
        if dic[int(lii[i][0] + 0.5)][int(lii[i][1] - 0.5)] != '3' and dic[int(lii[i][0] + 0.5)][
            int(lii[i][1] - 0.5)] != '1' and (lii[i][0] + 1, lii[i][1]) not in lii:
            count += 1
        if dic[int(lii[i][0] - 0.5)][int(lii[i][1] + 0.5)] != '3' and dic[int(lii[i][0] - 0.5)][
            int(lii[i][1] + 0.5)] != '2' and (lii[i][0], lii[i][1] + 1) not in lii:
            count += 1
        if count >= 2:
            lii.pop(i)
    return lii


def correct_cul(dic, li):
    count = 0
    record = {}
    cul = []
    for (i, j) in li:
        if dic[int(i - 0.5)][int(j - 0.5)] == '3' or dic[int(i - 0.5)][int(j - 0.5)] == '1':
            count += 1
        else:
            record.update({(i, j): 'up'})
        if dic[int(i - 0.5)][int(j - 0.5)] == '3' or dic[int(i - 0.5)][int(j - 0.5)] == '2':
            count += 1
        else:
            record.update({(i, j): 'left'})
        if dic[int(i + 0.5)][int(j - 0.5)] == '3' or dic[int(i + 0.5)][int(j - 0.5)] == '1':
            count += 1
        else:
            record.update({(i, j): 'down'})
        if dic[int(i - 0.5)][int(j + 0.5)] == '3' or dic[int(i - 0.5)][int(j + 0.5)] == '2':
            count += 1
        else:
            record.update({(i, j): 'right'})
        if count == 3:
            cul.append((i, j))
            if i - 0.5 >= 0 and i + 0.5 < len(dic) and j - 0.5 >= 0 and j + 0.5 < len(dic[0]):
                for (k, l) in record.keys():
                    if record[(k, l)] == 'left':
                        if dic[int(k - 0.5)][int(l - 0.5)] == '1':
                            dic[int(k - 0.5)][int(l - 0.5)] = '3'
                        else:
                            dic[int(k - 0.5)][int(l - 0.5)] = '2'
                    if record[(k, l)] == 'up':
                        if dic[int(k - 0.5)][int(l - 0.5)] == '2':
                            dic[int(k - 0.5)][int(l - 0.5)] = '3'
                        else:
                            dic[int(k - 0.5)][int(l - 0.5)] = '1'
                    if record[(k, l)] == 'down':
                        if dic[int(k + 0.5)][int(l - 0.5)] == '2':
                            dic[int(k + 0.5)][int(l - 0.5)] = '3'
                        else:
                            dic[int(k + 0.5)][int(l - 0.5)] = '1'
                    if record[(k, l)] == 'right':
                        if dic[int(k - 0.5)][int(l + 0.5)] == '1':
                            dic[int(k - 0.5)][int(l + 0.5)] = '3'
                        else:
                            dic[int(k - 0.5)][int(l + 0.5)] = '2'
        count = 0
        record = {}
    if len(cul) != 0:
        cul += correct_cul(dic, li)
    else:
        return {}
    return cul


def count_cha_areas(li, dic):
    count = {}
    for (i, j) in li:
        if (i - 1, j) not in li:
            if dic[int(i - 0.5)][int(j - 0.5)] != '1' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                count.update({(i, j): 'up'})
        if (i + 1, j) not in li:
            if dic[int(i + 0.5)][int(j - 0.5)] != '1' and dic[int(i + 0.5)][int(j - 0.5)] != '3':
                count.update({(i, j): 'down'})
        if (i, j - 1) not in li:
            if dic[int(i - 0.5)][int(j - 0.5)] != '2' and dic[int(i - 0.5)][int(j - 0.5)] != '3':
                count.update({(i, j): 'left'})
        if (i, j + 1) not in li:
            if dic[int(i - 0.5)][int(j + 0.5)] != '2' and dic[int(i - 0.5)][int(j + 0.5)] != '3':
                count.update({(i, j): 'right'})
    return count


def no_intersection_path(dic, dic_area, cul, door, green):
    lii = {}
    for i in range(len(door)):
        if door[i][0] == 0:
            dic_area.update({(door[i][0], door[i][1]): dic_area[(door[i][0] + 0.5, door[i][1])]})
        elif door[i][0] == len(dic) - 1:
            dic_area.update({(door[i][0], door[i][1]): dic_area[(door[i][0] - 0.5, door[i][1])]})
        elif door[i][1] == 0:
            dic_area.update({(door[i][0], door[i][1]): dic_area[(door[i][0], door[i][1] + 0.5)]})
        else:
            dic_area.update({(door[i][0], door[i][1]): dic_area[(door[i][0], door[i][1] - 0.5)]})
    for i in range(len(set(dic_area.values()))):
        li = []
        x_m = []
        y_m = []
        count = 0
        cou = 0
        for (j, k) in dic_area.keys():
            if (j, k) not in cul and dic_area[(j, k)] == i:
                li.append((j, k))
        if len(list(set(li).intersection(set(door)))) == 2:
            for l in range(len(li)):
                x_m.append(li[l][0])
                y_m.append(li[l][1])
            x_max = max(x_m)
            y_max = max(y_m)
            x_min = min(x_m)
            y_min = min(y_m)
            for (p, q) in green:
                if x_min <= p <= x_max and y_min <= q <= y_max:
                    count += 1
            if count < 2:
                for l in range(len(li)):
                    for m in range(len(li)):
                        if li[l][0] == li[m][0] and li[l][1] + 1 == li[m][1]:
                            cou += 1
                        if li[l][0] == li[m][0] and li[l][1] - 1 == li[m][1]:
                            cou += 1
                        if li[l][0] + 1 == li[m][0] and li[l][1] == li[m][1]:
                            cou += 1
                        if li[l][0] - 1 == li[m][0] and li[l][1] == li[m][1]:
                            cou += 1
                    if cou < 3:
                        if li[l][0] == 0:
                            lii.update({(-0.5, li[l][1]): i})
                        elif li[l][0] == len(dic) - 1:
                            lii.update({(len(dic) - 0.5, li[l][1]): i})
                        elif li[l][1] == 0:
                            lii.update({(li[l][0], -0.5): i})
                        elif li[l][1] == len(dic[0]) - 1:
                            lii.update({(li[l][0], len(dic[0]) - 0.5): i})
                        else:
                            lii.update({(li[l][0], li[l][1]): i})
    return lii