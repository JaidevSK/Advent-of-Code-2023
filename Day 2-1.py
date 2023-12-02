# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:38:04 2023

@author: jaidev
"""


file1 = open('Day2-1 Input.txt', 'r')
Lines = file1.readlines()
ids_lis = []
final_blue=[]
final_green=[]
final_red=[]

blue_limit = 14
green_limit = 13
red_limit = 12
good_ids=[]

for line in Lines:
    a = line.strip()
    id1 = a.split(": ")
    ids_lis.append(int((id1[0].split(" "))[-1]))
    
    balls = id1[1].split("; ")
    sub_games = []
    blue_lis=[]
    green_lis=[]
    red_lis=[]
    for ball in balls:
        ball2 = ball.split(", ")
        for ball3 in ball2:
            if 'blue' in ball3:
                blue_lis.append(int(ball3.split(" ")[0]))
            elif 'red' in ball3:
                red_lis.append(int(ball3.split(" ")[0]))
            elif 'green' in ball3:
                green_lis.append(int(ball3.split(" ")[0]))
    final_red.append(max(red_lis))
    final_blue.append(max(blue_lis))
    final_green.append(max(green_lis))
    
for i in range(len(ids_lis)):
    if final_red[i]<=red_limit and final_blue[i]<=blue_limit and final_green[i]<=green_limit:
        good_ids.append(ids_lis[i])
        
print("The answer to Day 2 Part 1 is:",sum(good_ids))


    
        
    