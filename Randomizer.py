import random
import form

def rand_form(TAB,LIST):
    sum = 0
    L = []
    for i in range(len(LIST)):
        L.append([LIST[i][0],LIST[i][1]])
    for i in L :
        sum += i[1]
    for i in range(len(L)):
        L[i][1] = L[i][1]/sum
    L1 = []
    L2 = []
    for i in range(len(L)):
        L1.append(L[i][0])
        L2.append(L[i][1])
    
    for i in range(len(TAB)):
        randomList = random.choices(L1,L2,k=len(TAB[0]))
        for j in range(len(TAB[0])):
            if TAB[i][j] == '*':
                TAB[i][j] = randomList[j]
    return TAB