# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 19:04:56 2023

@author: jaidev
"""


file1 = open('Day4-1 Input.txt', 'r')
Lines = file1.readlines()
score_lis=[]

for line in Lines:
    a=line.strip()
    winning = (a.split("|")[0]).split(":")[1]
    winning_final = winning.strip().split(" ")
    total = set(a.split("|")[1].strip().split(" "))
    present=False
    winning_final1=[]
    for i in range(len(winning_final)):
        if winning_final[i]!='':
            winning_final1.append(winning_final[i])
    for i in range(len(winning_final1)):        
        if winning_final1[i] in total:
                present=True
        if present==False:
            score=0
        else:
            score_power=-1
            for i in range(len(winning_final1)):
                if winning_final1[i] in total:
                    score_power+=1
            score=2**(score_power)
        
    score_lis.append(score)
    
print(score_lis)
print("The Answer to Day 4 Part 1 is",sum(score_lis))
    