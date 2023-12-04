# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 19:37:46 2023

@author: jaide
"""
from queue import Queue

q=Queue()

file1 = open('Day4-2 Input.txt', 'r')
Lines = file1.readlines()
score_lis=[]
card_lis=[]
card_ctr=[1]*220
card_dict={}
ans=0

for line in Lines:
    a=line.strip()    
    cid, numbers = line.split(':')
    cid = int(cid[4:])
    winning = (a.split("|")[0]).split(":")[1]
    winning_final = winning.strip().split(" ")
    total = list(a.split("|")[1].strip().split(" "))
    present=False
    winning_final1=[]
    ourtotal1=[]
    card_no=int(((a.split("|")[0]).split(":")[0])[4:])
    card_lis.append(card_no)
    for i in range(len(winning_final)):
        if winning_final[i]!='':
            winning_final1.append(winning_final[i])
    for i in range(len(total)):
        if total[i]!='':
            ourtotal1.append(total[i])

    ours=set(ourtotal1)
    winnign=set(winning_final1)       
    matched=ours & winnign
    card_dict[cid] = len(matched)
    q.put(cid)
 
 
while not q.empty():
    ans += 1
    k = q.get()
    for i in range(k + 1, k + card_dict[k] + 1):
        q.put(i)

print("The Answer for Day 4 Part 2 is",ans)  