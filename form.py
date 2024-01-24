import math

def defineTab(L,l):
    if(L == 0) :
        return [[]]
    tab = [['.' for j in range(L)] for i in range(l)]
    return tab

def circle(r):
    width, height = 2*r+1,2*r+1
    tab = defineTab(width,height)
    
    EPSILON = 3.5

    # draw the circle
    for y in range(height):
        for x in range(width):
            # see if we're close to (x-a)**2 + (y-b)**2 == r**2
            if abs((x-r)**2 + (y-r)**2 - r**2) < EPSILON**2:
                tab[y][x] = '*'
    return tab

def disk(r):
    width, height = 2*r+1,2*r+1
    tab = defineTab(width,height)
    
    EPSILON = 1.5

    # draw the circle
    for y in range(height):
        for x in range(width):
            # see if we're close to (x-a)**2 + (y-b)**2 == r**2
            if abs((x-r)**2 + (y-r)**2) < r**2-EPSILON:
                tab[y][x] = '*'
    return tab