import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
res=9999
if(n==0):
    print("0")
else:
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        if(abs(t)<abs(res)):
            res=t
        elif abs(t)==abs(res) and t>res:
            res=t
    print(res)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)