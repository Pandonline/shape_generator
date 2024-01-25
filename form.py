import math

def defineTab(L,l,c='.'):
    if(L == 0) :
        return [[]]
    tab = [[c for j in range(L)] for i in range(l)]
    return tab

def circle(r):
    width, height = 2*r+1,2*r+1
    tab = defineTab(width,height)
    # draw the circle
    for y in range(height):
        for x in range(width):
            # see if we're close to (x-a)**2 + (y-b)**2 == r**2
            if abs((x-r)**2 + (y-r)**2) > (r-0.5)**2 and abs((x-r)**2 + (y-r)**2) < (r+0.5)**2:
                tab[y][x] = '*'
    return tab

def disk(r):
    width, height = 2*r+1,2*r+1
    tab = defineTab(width,height)
    # draw the circle
    for y in range(height):
        for x in range(width):
            # see if we're close to (x-a)**2 + (y-b)**2 == r**2
            if abs((x-r)**2 + (y-r)**2) < (r+0.5)**2:
                tab[y][x] = '*'
    return tab

def square(l):
    return defineTab(l,l,"*")

def rect(L,l):
    return defineTab(L,l,"*")

def pp(tab):
    for line in tab:
        print(' '.join(line))