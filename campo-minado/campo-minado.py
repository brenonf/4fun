
def tabuleiro(n):
    m = list()
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(' # ')
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
    print('\n')


def espelho(m):
    mb = list()
    mb = deepcopy(m)
    return mb

    
def bomba(mb,quant):
    n = len(mb)
    for i in range(n):
        for j in range(n):
            mb[j][i] = '   '
    for i in range(quant):
        while True:
            x = ri(0, n-1)
            y = ri(0, n-1)
            if mb[x][y] != '   ':
                continue
            else:
                mb[x][y] = '[B]'
                break
    return mb


def jogada(m,mb):
    while True:
        print('Faça sua jogada')
        l = int(input('Digite a linha: ')) - 1
        c = int(input('Digite a coluna: ')) - 1
        if m[l][c] == ' # ':
            if mb[l][c] != '[B]':
                m[l][c] = mb[l][c]
                impressao(m)
            elif mb[l][c] == '[B]':
                print('Você explodiu !!!!')
                break
        else:
            print('Essa célula já foi escolhida !')
            continue
            
def numeros_bomba(mb):
    n = len(mb)
    for i in range(n):
        for j in range(n):
            if mb[i][j] != '[B]'
                cont = 0
            
    
    
from copy import deepcopy
from random import randint as ri
m = tabuleiro(6)
mb = espelho(m)
print()
mb = bomba(mb,12)
print()
impressao(mb)






'''
imprimir assim no futuro:
     0     1     2     3
   +-----+-----+-----+-----+
0  | 11  | -3  |  4  |  8  |
   +-----+-----+-----+-----+
1  | -3  | 12  |  6  | 11  |
   +-----+-----+-----+-----+
2  |  4  |  6  |  5  | 13  |
   +-----+-----+-----+-----+
3  |  8  | 11  | 13  |  5  |
   +-----+-----+-----+-----+

'''
