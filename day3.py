#python3

"""advent of code day 3
rucksack problem
use file day3.txt
"""
file_in = "day3.txt"

def new_order(letter):
    order = ord(letter)
    if order > 91:
        return order - 64
    else:
        return order - 38

data = []
with open(file_in) as fin:
    line = fin.readline()
    line1, line2 = line[:len(line)/2], line[len(line)/2:]
    data.append([line1,line2])

for datum in data:
    for chr in datum[0]:
        pass