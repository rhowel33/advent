#python3

"""
Take in a file of that lists the elf's suggested strategy
Each elf is seperated from the last via a blank line.

Use day2.txt as input file

"""
import numpy as np

file_in = "day2.txt"
data = []
with open(file_in) as fin:
    for line in fin.readlines():
        data.append([*line[::2]])


rock = 1
paper = 2
scissors = 3

loss = 0
win = 6
draw = 3

#comparisons
def winner(them, you):
    if them == "A":
        them = 1
    elif them == "B":
        them = 2
    elif them == "C":
        them = 3
    if you == "X":
        you = 1
    elif you == "Y":
        you = 2
    elif you == "Z":
        you = 3
    if you == them:
        return 3
    elif you == 3 and them == 1:
        return 0
    elif you == 1 and them == 2:
        return 0
    elif you == 2 and them == 3:
        return 0
    else:
        return 6

scores = []

for datum in data:

    if datum[1] == "X":
        term2 = 1
    elif datum[1] == "Y":
        term2 = 2
    elif datum[1] == "Z":
        term2 = 3
    scores.append(term2 + winner(*datum))

print(sum(scores))

#part2
#there is a clarification and the x y z tell you how to end the round
#x means lose
#y means draw
#z means win

def true_winner(them, you):
    if you == "X":
        if them == "A":
            return 3
        elif them == "B":
            return 1
        elif them =="C":
            return 2
    elif you == "Y":
        if them == "A":
            return 1 + 3
        elif them == "B":
            return 2 +3
        elif them =="C":
            return 3 + 3
    elif you == "Z":
        if them == "A":
            return 2 +6
        elif them == "B":
            return 3 + 6
        elif them =="C":
            return 1 + 6
new_score = []
for datum in data:
    new_score.append(true_winner(*datum))

print(sum(new_score))