import sys
import math


def attraction_less_than_l(text, index,mem_dict, answer):
    current_index=index
    day_ride=0
    amount = 0
    while day_ride+text[index]<=l:
        day_ride += text[index]
        answer += text[index]
        amount += text[index]
        temp_calc = (index+1)%len(text)
        index = temp_calc
        if index != current_index:
            continue
        else:
            break
    mem_dict[current_index] = [amount, index]
    return text,index,current_index,mem_dict,answer

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
l, c, n = [int(i) for i in input().split()]
text = []
mem_dict = {}
index = 0
answer = 0

for i in range(n):
    pi = int(input())
    text.append(pi)

while c > 0:
    current_index = index
    day_ride = 0
    try:
        answer += mem_dict[index][0]
        index = mem_dict[index][1]
    except KeyError:
        text,index,current_index,mem_dict,answer=attraction_less_than_l(text, index,mem_dict, answer)
    c-=1

print(answer)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)