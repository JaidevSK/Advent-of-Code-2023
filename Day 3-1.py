# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:08:14 2023

@author: jaidev
"""


file1 = open('Day3-1 Input.txt', 'r')
Lines = file1.readlines()
spl_char={'!','@','#','$','%','&','/','?','*','+','=','-','_','|','}','{',']','[',':','~','*'}
ints={'0','1','2','3','4','5','6','7','8','9'}
left=[]
right=[]
up=[]
down=[]
diag=[]
downright=[]
downleft=[]
upright=[]
upleft=[]

for j in range(len(Lines)):
    line=Lines[j]
    for i in range(len(line)):
        if line[i] in spl_char:
            if line[i+1] in ints:
                a=''
                ctr=1
                while ctr+i<len(line) and line[i+ctr]!='.':
                    a=a+line[i+ctr]
                    ctr+=1
                right.append(int(a))
            if line[i-1] in ints:
                a=''
                ctr=1
                while ctr<=i and line[i-ctr]!='.':
                    a=a+line[i-ctr]
                    ctr+=1
                #print(a[::-1])
                left.append(int(a[::-1]))
                
            if j>0 and Lines[j-1][i] in ints:
                a=Lines[j-1][i]
                ctr=1
                while ctr<=i and Lines[j-1][i-ctr]!='.':
                    a=a+Lines[j-1][i-ctr]
                    ctr+=1
                lef=a[::-1]
                b=''
                ctr=1
                while ctr+i<len(line) and Lines[j-1][i+ctr]!='.':
                    b=b+Lines[j-1][i+ctr]
                    ctr+=1
                rig=b
                up.append(int(lef+rig))
                
            if j<len(Lines) and Lines[j+1][i] in ints:
                a=Lines[j+1][i]
                ctr=1
                while ctr<=i and Lines[j+1][i-ctr]!='.':
                    a=a+Lines[j+1][i-ctr]
                    ctr+=1
                lef=a[::-1]
                b=''
                ctr=1
                while ctr+i<len(line) and Lines[j+1][i+ctr]!='.':
                    b=b+Lines[j+1][i+ctr]
                    ctr+=1
                rig=b
                down.append(int(lef+rig))
                
            if j<len(Lines) and Lines[j+1][i+1] in ints:
                if Lines[j+1][i]=='.':
                    b=''
                    ctr=1
                    while ctr+i<len(line) and Lines[j+1][i+ctr]!='.':
                        b=b+Lines[j+1][i+ctr]
                        ctr+=1
                    rig=b
                    downright.append(int(rig))
                
            if j<len(Lines) and Lines[j+1][i-1] in ints:
                if Lines[j+1][i]=='.':
                    a=''
                    ctr=1
                    while ctr<=i and Lines[j+1][i-ctr]!='.':
                        a=a+Lines[j+1][i-ctr]
                        ctr+=1
                    lef=a[::-1]
                    downleft.append(int(lef))
            
            if j>0 and Lines[j-1][i-1] in ints:
                if Lines[j-1][i]=='.':
                    a=''
                    ctr=1
                    while ctr<=i and Lines[j-1][i-ctr]!='.':
                        a=a+Lines[j-1][i-ctr]
                        ctr+=1
                    lef=a[::-1]
                    upleft.append(int(lef))
                
            if j>0 and Lines[j-1][i+1] in ints:
                if Lines[j-1][i]=='.':
                    b=''
                    ctr=1
                    while ctr+i<len(line) and Lines[j-1][i+ctr]!='.':
                        b=b+Lines[j-1][i+ctr]
                        ctr+=1
                    rig=b
                    upright.append(int(rig))
                
            
                
print("Down =", down)
print("Up =", up)
print("Left =", left)
print("Right =", right)
print("Down Right =", downright)
print("Down Left =", downleft)
print("Up Left =", upleft)
print("Up Right =", upright)

print("The answer for Day 3 Part 1 is", sum(right)+sum(left)+sum(up)+sum(down)+sum(downleft)+sum(downright)+sum(upleft)+sum(upright))

                
            