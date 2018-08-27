
def tabuleiro(n):
    m = list()
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append('[ ]')
    cont = 1
    for i in range(n):
        print('|',end='')
        for j in range(n):
            if cont <= 9:
                print('{}'.format(m[i][j]),end='')
            elif cont >= 10 and cont < 100:
                print('{}'.format(m[i][j]),end='')
            else:
                print('{}'.format(m[i][j]),end='')
            print('|',end='')
            cont += 1
        print(' ',i + 1)
    for i in range(1,n+1):
        if i < 9:
            print(' ',end=' ')
            print(i,end=' ')
        elif i == 9:
            print(' ',end=' ')
            print(i,end=' ')
        elif i > 9 and i < 100:
            print(' ',end=' ')
            print(i,end='')
    return m


def impressao(m):
    n = len(m)
    cont = n ** 2 + 1
    for i in range(n):
        print('|',end='')
        for j in range(n):
            if cont <= 9:
                print('{}'.format(m[i][j]),end='')
            elif cont >= 10 and cont < 100:
                print('{}'.format(m[i][j]),end='')
            else:
                print('{}'.format(m[i][j]),end='')
            print('|',end='')
            cont += 1
        print(' ',i + 1)
    for i in range(1,n+1):
        if i < 9:
            print(' ',end=' ')
            print(i,end=' ')
        elif i == 9:
            print(' ',end=' ')
            print(i,end=' ')
        elif i > 9 and i < 100:
            print(' ',end=' ')
            print(i,end='')
    return m


def bomba(m,quant):
    n = len(m)
    for i in range(quant):
        while True:
            x = ri(0, n-1)
            y = ri(0, n-1)
            if m[x][y] != '[ ]':
                continue
            else:
                m[x][y] = '[*]'
                break
    return m
        
from random import randint as ri
m = tabuleiro(6)
print()
m = bomba(m,30)
print()
impressao(m)
