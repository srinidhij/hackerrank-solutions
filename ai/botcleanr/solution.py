#!/usr/bin/python
from math import sqrt
def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print 'CLEAN'
        return
    i = 0
    j = 0
    dirtypos = []
    while i < 5:
        j = 0
        while j < 5:
            if board[i][j] == 'd':
                dirtypos.append((i,j))
            j += 1
        i += 1
    leastd = 99999
    t = None
    for d in dirtypos:
        dist = sqrt((posr-d[0])**2 + (posc-d[1])**2)
        if dist < leastd:
            leastd = dist
            t = d

    #print t
    #print posr, posc

    if (posr - t[0]) == 0:
        direction = 1
    elif (posc - t[1    ]) == 0:
        direction = 0
    else:
        direction = 1 if abs(posr - t[0]) <= abs(posc - t[1]) else 0

    #print direction
    #print 'posc, t[1] = ', posc, t[1]
    #print 'posr, t[0] = ', posr, t[0]

    if direction == 1:
        if posc > t[1]:
            print 'LEFT'
        else :
            print 'RIGHT'
    if direction == 0:
        if posr > t[0]:
            print 'UP'
        else:
            print 'DOWN'

if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)