# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:05:24 2023

@author: jaide
"""


file1 = open('Day2-2 Input.txt', 'r')
Lines = file1.readlines()
ids_lis = []
final_blue=[]
final_green=[]
final_red=[]
power_lis=[]


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
    power_lis.append(final_red[i]*final_blue[i]*final_green[i])
    
#print(power_lis)
        
print("The answer to Day 2 Part 2 is:",sum(power_lis))

