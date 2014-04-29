#!/bin/python
def nextMove(n,a,b,grid):
#print all the moves here
    i = j = 0
    botp = pp = None
    while i < n:
        j = 0
        while j < n:
            if grid[i][j] == 'p':
                pp = (i,j)
                break
            j += 1
            if pp:
                break 
        i += 1

    botp = (a,b)
    ydiff = botp[0] - pp[0]
    xdiff = botp[1] - pp[1]
    

    if xdiff == 0:
        pass

    elif xdiff < 0:
        return 'RIGHT'
        xdiff += 1

    else:
        return 'LEFT'
        xdiff -= 1

    if ydiff == 0:
        pass

    elif ydiff < 0 :
        return 'DOWN'
        ydiff += 1
    else :
        return 'UP'
        ydiff -= 1

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
