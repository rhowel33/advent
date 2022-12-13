#python 3

"""
Take in a file of that lists the calories per meal for each elf.
Each elf is seperated from the last via a blank line.

Use day1.txt as input file

"""
import numpy as np

#part1
filein = "day1.txt"

with open(filein) as fin:
    data = fin.readlines()

elves = []
new_elf = True
for i,cals in enumerate(data):
    if new_elf:
        elves.append(float(cals))
        new_elf = False

    else:
        if cals == '\n':
            new_elf = True
        else:
            elves[-1] += float(cals)




print(f'the most cals carried is {max(elves)}')


#part2
#Find the total calories carried by the top 3 calories carrying elves

elves.sort(reverse=True)

print(f"the top 3 elves have {sum(elves[:3])} calories")