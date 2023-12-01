# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:35:32 2023

@author: jaidev
"""


file1 = open('Day1-1 Input.txt', 'r')
Lines = file1.readlines()

nums_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
nums_lis = []

for line in Lines:
#    print(line.strip())
    
    if line == '\n':
        pass
    else:
        for i in range(len(line)):
            if line[i] in nums_set:
                a=line[i]
                break
        for j in range(len(line)-1, -1, -1):
            if line[j] in nums_set:
                b=line[j]
                break
        nums_lis.append(int(a+b))

print("The answer to Day 1 Problem 1 is:", sum(nums_lis))

#54953