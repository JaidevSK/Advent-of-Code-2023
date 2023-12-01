# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 23:06:18 2023

@author: jaidev
"""

file1 = open('Day1-2 Input.txt', 'r')
Lines = file1.readlines()
nums_lis = []

for line in Lines:
#    print(line.strip())
    if line == '\n':
        pass
    else:
        for i in range(len(line)):
            if line[i:i+3]=='one' or line[i]=='1':
                a=10
                break
            elif line[i:i+3]=='two' or line[i]=='2':
                a=20
                break
            elif line[i:i+5]=='three' or line[i]=='3':
                a=30
                break
            elif line[i:i+4]=='four' or line[i]=='4':
                a=40
                break
            elif line[i:i+4]=='five' or line[i]=='5':
                a=50
                break
            elif line[i:i+3]=='six' or line[i]=='6':
                a=60
                break
            elif line[i:i+5]=='seven' or line[i]=='7':
                a=70
                break
            elif line[i:i+5]=='eight' or line[i]=='8':
                a=80
                break
            elif line[i:i+4]=='nine' or line[i]=='9':
                a=90
                break
            
        line2 = line[::-1] ## Reversing the string and checking in the reversed string
                    
        for i in range(len(line2)):
            if line2[i:i+3]=='eno' or line2[i]=='1':
                b=1
                break
            elif line2[i:i+3]=='owt' or line2[i]=='2':
                b=2
                break
            elif line2[i:i+5]=='eerht' or line2[i]=='3':
                b=3
                break
            elif line2[i:i+4]=='ruof' or line2[i]=='4':
                b=4
                break
            elif line2[i:i+4]=='evif' or line2[i]=='5':
                b=5
                break
            elif line2[i:i+3]=='xis' or line2[i]=='6':
                b=6
                break
            elif line2[i:i+5]=='neves' or line2[i]=='7':
                b=7
                break
            elif line2[i:i+5]=='thgie' or line2[i]=='8':
                b=8
                break
            elif line2[i:i+4]=='enin' or line2[i]=='9':
                b=9
                break

        nums_lis.append(a+b)

print("The answer for Day 1 Part 2 is:", sum(nums_lis))

#53868
                