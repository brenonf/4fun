from copy import deepcopy
from random import randint as ri

def tabuleiro(n):
    """Cria um tabuleiro vazio de tamanho n x n."""
    m = []
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(' # ')
    cont = 1
    for i in range(n):
        print('|', end='')
        for j in range(n):
            if cont <= 9:
                print('{}'.format(m[i][j]), end='')
            elif cont >= 10 and cont < 100:
                print('{}'.format(m[i][j]), end='')
            else:
                print('{}'.format(m[i][j]), end='')
            print('|', end='')
            cont += 1
        print(' ', i + 1)
    for i in range(1, n + 1):
        if i < 9:
            print(' ', end=' ')
            print(i, end=' ')
        elif i == 9:
            print(' ', end=' ')
            print(i, end=' ')
        elif i > 9 and i < 100:
            print(' ', end=' ')
            print(i, end='')
    return m

def impressao(m):
    """Imprime o tabuleiro."""
    n = len(m)
    cont = n ** 2 + 1
    for i in range(n):
        print('|', end='')
        for j in range(n):
            if cont <= 9:
                print('{}'.format(m[i][j]), end='')
            elif cont >= 10 and cont < 100:
                print('{}'.format(m[i][j]), end='')
            else:
                print('{}'.format(m[i][j]), end='')
            print('|', end='')
            cont += 1
        print(' ', i + 1)
    for i in range(1, n + 1):
        if i < 9:
            print(' ', end=' ')
            print(i, end=' ')
        elif i == 9:
            print(' ', end=' ')
            print(i, end=' ')
        elif i > 9 and i < 100:
            print(' ', end=' ')
            print(i, end='')
    print('\n')

def espelho(m):
    """Cria uma cópia do tabuleiro."""
    return deepcopy(m)

def bomba(mb, quant):
    """Distribui bombas aleatoriamente pelo tabuleiro."""
    n = len(mb)
    for i in range(n):
        for j in range(n):
            mb[j][i] = '   '
    for i in range(quant):
        while True:
            x = ri(0, n - 1)
            y = ri(0, n - 1)
            if mb[x][y] != '   ':
                continue
            else:
                mb[x][y] = '[B]'
                break
    return mb

def jogada(m, mb):
    """Executa a jogada do jogador."""
    num_bombas = sum(row.count('[B]') for row in mb)  # Conta o número de bombas no tabuleiro
    celulas_sem_bomba = len(m) * len(m) - num_bombas
    celulas_reveladas = 0
    while True:
        print('Faça sua jogada')
        l = int(input('Digite a linha: ')) - 1
        c = int(input('Digite a coluna: ')) - 1
        if m[l][c] == ' # ':
            if mb[l][c] != '[B]':
                m[l][c] = mb[l][c]
                impressao(m)
                celulas_reveladas += 1
                if celulas_reveladas == celulas_sem_bomba:
                    print('Parabéns, você ganhou!')
                    return False  # Indica que o jogador ganhou o jogo
            else:
                print('Você explodiu !!!!')
                revelar_bombas(m, mb)
                impressao(m)
                return False  # Indica que o jogo deve encerrar
        else:
            print('Essa célula já foi escolhida !')
            continue





def numeros_bomba(mb):
    """Conta o número de bombas ao redor de cada célula."""
    n = len(mb)
    for i in range(n):
        for j in range(n):
            if mb[i][j] != '[B]':
                cont = 0
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if 0 <= i + a < n and 0 <= j + b < n:
                            if mb[i + a][j + b] == '[B]':
                                cont += 1
                mb[i][j] = ' {} '.format(cont) if cont != 0 else '   '
    return mb

def revelar_bombas(m, mb):
    """Revela todas as bombas no tabuleiro."""
    n = len(mb)
    for i in range(n):
        for j in range(n):
            if mb[i][j] == '[B]':
                m[i][j] = '[B]'

def iniciar_jogo():
    """Inicia o jogo de Campo Minado."""
    tamanho = int(input("Digite o tamanho do tabuleiro: "))
    quantidade_bombas = int(input("Digite a quantidade de bombas: "))
    
    m = tabuleiro(tamanho)
    mb = espelho(m)
    mb = bomba(mb, quantidade_bombas)
    mb = numeros_bomba(mb)
    
    while True:
        if not jogada(m, mb):  # Se a jogada resultar em uma explosão, encerra o jogo
            break
        if ' # ' not in [celula for linha in m for celula in linha]:
            print("Parabéns! Você venceu!")
            break

if __name__ == "__main__":
    iniciar_jogo()
