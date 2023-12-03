# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:38:35 2023

@author: jaidev
"""


file1 = open('Day3-2 Input.txt', 'r')
Lines = file1.readlines()
spl_char={'*'}
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

lis_final=[]

for j in range(len(Lines)):
    line=Lines[j]
    for i in range(len(line)):
        if line[i] in spl_char:
            rightexists=False
            leftexists=False
            upleftexists=False
            downleftexists=False
            uprightexists=False
            downrightexists=False
            downexists=False
            upexists=False
            if line[i+1] in ints:
                a=''
                ctr=1
                while ctr+i<len(line) and line[i+ctr]!='.':
                    a=a+line[i+ctr]
                    ctr+=1
                right.append(int(a))
                rightexists=True
            if line[i-1] in ints:
                a=''
                ctr=1
                while ctr<=i and line[i-ctr]!='.':
                    a=a+line[i-ctr]
                    ctr+=1
                #print(a[::-1])
                left.append(int(a[::-1]))
                leftexists=True
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
                upexists=True
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
                downexists=True
            if j<len(Lines) and Lines[j+1][i+1] in ints:
                if Lines[j+1][i]=='.':
                    b=''
                    ctr=1
                    while ctr+i<len(line) and Lines[j+1][i+ctr]!='.':
                        b=b+Lines[j+1][i+ctr]
                        ctr+=1
                    rig=b
                    downright.append(int(rig))
                    downrightexists=True
            if j<len(Lines) and Lines[j+1][i-1] in ints:
                if Lines[j+1][i]=='.':
                    a=''
                    ctr=1
                    while ctr<=i and Lines[j+1][i-ctr]!='.':
                        a=a+Lines[j+1][i-ctr]
                        ctr+=1
                    lef=a[::-1]
                    downleft.append(int(lef))
                    downleftexists=True
            if j>0 and Lines[j-1][i-1] in ints:
                if Lines[j-1][i]=='.':
                    a=''
                    ctr=1
                    while ctr<=i and Lines[j-1][i-ctr]!='.':
                        a=a+Lines[j-1][i-ctr]
                        ctr+=1
                    lef=a[::-1]
                    upleft.append(int(lef))
                    upleftexists=True
            if j>0 and Lines[j-1][i+1] in ints:
                if Lines[j-1][i]=='.':
                    b=''
                    ctr=1
                    while ctr+i<len(line) and Lines[j-1][i+ctr]!='.':
                        b=b+Lines[j-1][i+ctr]
                        ctr+=1
                    rig=b
                    upright.append(int(rig))
                    uprightexists=True
                    
            #print(upleftexists, upexists, uprightexists, rightexists, downrightexists, downexists, downleftexists, leftexists)
            
            if upexists and downexists:
                lis_final.append(up[-1]*down[-1])
            if upexists and downleftexists:
                lis_final.append(up[-1]*downleft[-1])
            if upexists and downrightexists:
                lis_final.append(up[-1]*downright[-1])
            if upexists and upleftexists:
                lis_final.append(up[-1]*upleft[-1])
            if upexists and uprightexists:
                lis_final.append(up[-1]*upright[-1])
            if upexists and leftexists:
                lis_final.append(up[-1]*left[-1])
            if upexists and rightexists:
                lis_final.append(up[-1]*right[-1])
            if downexists and downleftexists:
                lis_final.append(down[-1]*downleft[-1])
            if downexists and downrightexists:
                lis_final.append(down[-1]*downright[-1])
            if downexists and upleftexists:
                lis_final.append(down[-1]*upleft[-1])
            if downexists and uprightexists:
                lis_final.append(down[-1]*upright[-1])
            if downexists and leftexists:
                lis_final.append(down[-1]*left[-1])
            if downexists and rightexists:
                lis_final.append(down[-1]*right[-1])
            if leftexists and downleftexists:
                lis_final.append(left[-1]*downleft[-1])
            if leftexists and downrightexists:
                lis_final.append(left[-1]*downright[-1])
            if leftexists and upleftexists:
                lis_final.append(left[-1]*upleft[-1])
            if leftexists and uprightexists:
                lis_final.append(left[-1]*upright[-1])
            if leftexists and rightexists:
                lis_final.append(left[-1]*right[-1])
            if rightexists and upleftexists:
                lis_final.append(right[-1]*upleft[-1])
            if rightexists and uprightexists:
                lis_final.append(right[-1]*upright[-1])
            if rightexists and downleftexists:
                lis_final.append(right[-1]*downleft[-1])
            if rightexists and downrightexists:
                lis_final.append(right[-1]*downright[-1])
            if downrightexists and downleftexists:
                lis_final.append(downright[-1]*downleft[-1])
            if uprightexists and downrightexists:
                lis_final.append(upright[-1]*downright[-1])
            if upleftexists and downleftexists:
                lis_final.append(upleft[-1]*downleft[-1])
            if upleftexists and downrightexists:
                lis_final.append(upleft[-1]*downright[-1])
            if uprightexists and downleftexists:
                lis_final.append(upright[-1]*downleft[-1])
            if upleftexists and uprightexists:
                lis_final.append(upleft[-1]*upright[-1])
                
#print(lis_final)
print("The answer for Day 3 Part 2 is", sum(lis_final))