#!/usr/bin/env python
# filename: pytsort.py
import os, sys

full=[]
'''
Desc: 判断需要读取什么文件，并读取
文件格式要求： 2列，中间空一格(多个空格也能处理)， col1 依赖 col2 
------file sample start-------
a b
alen alex
b Bob
b c
c xyz
------file sample start-------
'''
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = os.path.dirname(__file__)+"/demo_data.txt"
    if not os.path.exists(filename):
        print("Please set file name as parameter 'pytsort.py <filename>', \n or create a default file in name 'pytsort_data.txt' in the same folder. ")
        exit()

with open(filename,"r") as f:
    for f_line in f:
        l_line = f_line.split()                       # old: f_line.strip().split(" ")
        if len(l_line) > 0:
	        full.append([l_line[0], l_line[1]])

while True: 
    row_num=len(full)

    '''准备set，取第各列数据'''
    col1=set()                       # full value of column 1
    col2=set()                       # full value of column 2
    for i in range(row_num):
        leni = len(full[i])
        if leni == 0:
            continue
        elif leni == 1:
            col1.add(full[i][0])
        elif leni == 2:
            col1.add(full[i][0])
            col2.add(full[i][1])

    col1readcopy=col1.copy()           # set 在循环过程中，不能变化，所以复制一个新 set

    '''取第一列数据，在第二列中找到相同值，表示被依赖，需要剔除； 最后剩下的是，无被依赖关系的元素'''
    for e in col1readcopy:                   # e means element
        if e in col2:
            col1.discard(e)

    ''' 清理全量数据 '''
    x = 0
    while x < row_num:
        if len(full[x]) == 0:
            full.pop(x)
            #print("pop line: ", x)
            row_num -= 1
            continue
        elif full[x][0] in col1:
            full[x].pop(0)
            #print("pop 1st element at line: ", x)
        x += 1
    
    if len(col1) == 0 :   
        if len([i for i in full if len(i)>0]) > 0:        #若无被依赖的元素数量为0,则表示完成查找，或者碰到循环依赖
            print("Dependency loop found， impacted data: ", full)
        break

    print(" ".join(col1))    #update format from "{'bob', 'dan'}" to "bob dan"

    '''list 中的空值不计算在 len 中'''
    if len(full) == 0:
        break