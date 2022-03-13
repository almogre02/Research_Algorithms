import sys
import math

# Solve this puzzle by writing the shortest code.
# Whitespaces (spaces, new lines, tabs...) are counted in the total amount of chars.
# These comments should be burnt after reading!

# lx: the X position of the light of power
# ly: the Y position of the light of power
# tx: Thor's starting X position
# ty: Thor's starting Y position
lx, ly, tx, ty = [int(i) for i in input().split()]

# game loop
while True:
    remainingTurns = int(input())
    X_path = ""
    Y_path = ""

    if ty < ly:  # goes down
        Y_path += "S"
        ty += 1
    elif ty > ly:  # goes up
        Y_path += "N"
        ty -= 1

    if tx < lx:  # goes right
        X_path += "E"
        tx -= 1
    elif tx > lx:  # goes left
        X_path += "W"
        tx += 1

    print(Y_path + X_path)

    # A single line providing the move to be made: N NE E SE S SW W or NW
