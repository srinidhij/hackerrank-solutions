#!/bin/python
def displayPathtoPrincess(n,grid):
#print all the moves here
    i = j = 0
    botp = pp = None
    while i < n:
        j = 0
        while j < n:
            if grid[i][j] == 'm':
                botp = (i,j)
            elif grid[i][j] == 'p':
                pp = (i,j)
            j += 1 
        i += 1

    ydiff = botp[0] - pp[0]
    xdiff = botp[1] - pp[1]
    

    if xdiff == 0:
        pass

    elif xdiff < 0:
        while xdiff < 0:
            print 'RIGHT'
            xdiff += 1

    else:
        while xdiff > 0 :
            print 'LEFT'
            xdiff -= 1

    if ydiff == 0:
        pass

    elif ydiff < 0 :
        while ydiff < 0:
            print 'DOWN'
            ydiff += 1
    else :
        while ydiff > 0 :
            print 'UP'
            ydiff -= 1

m = input()
grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
