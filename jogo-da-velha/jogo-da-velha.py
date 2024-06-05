import os
from random import randint
import time

def escolha():
    p = 999
    print('Escolha com qual caractere vai jogar.')
    while p != 'x' and p != 'o':
        p = input("x ou o: ")
        p = p.lower()
        if p != 'x' and p != 'o':
            print('Os valores "x" ou "o" não foram encontrados, tente de novo!!!')
            print()
    print('Você escolheu {}!'.format(p))
    if p == 'x':
        c = 'o'
    else:
        c = 'x'
    return p, c


def base_do_jogo():
    a = dict()
    cont = 1
    for i in range(9):
        a[cont] = cont
        cont += 1
    return a


def jogada(player, a):
    while True:
        print('Faça sua jogada escolhendo as posições disponíveis')
        cont = 1
        for i in range(3):
            print(a[cont], '|', a[cont + 1], '|', a[cont + 2])
            cont += 3        
        joga = input('Digite um número de 1 a 9: ')
        if joga not in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            print()
            continue
        joga = int(joga)
        if a[joga] in {'x', 'o'}:
            print('O campo já foi escolhido')
            continue
        a[joga] = player
        cont = 1
        for i in range(3):
            print(a[cont], '|', a[cont + 1], '|', a[cont + 2])
            cont += 3
        break
    print()
    return a
        

def conferir(player, a):
    #linha
    w = 0
    if (a[1] == player and a[2] == player and a[3] == player or
        a[4] == player and a[5] == player and a[6] == player or
        a[7] == player and a[8] == player and a[9] == player or
        #coluna
        a[1] == player and a[4] == player and a[7] == player or
        a[2] == player and a[5] == player and a[8] == player or
        a[3] == player and a[6] == player and a[9] == player or
        #diagonais
        a[1] == player and a[5] == player and a[9] == player or
        a[3] == player and a[5] == player and a[7] == player):
        w = player

    return player if w else 0


def avaliar(a):
    #Checar linhas
    for row in [1, 4, 7]:
        if a[row] == a[row + 1] == a[row + 2]:
            if a[row] == 'x':
                return 10
            elif a[row] == 'o':
                return -10
    
    #Checar colunas
    for col in [1, 2, 3]:
        if a[col] == a[col + 3] == a[col + 6]:
            if a[col] == 'x':
                return 10
            elif a[col] == 'o':
                return -10
    
    #Checar diagonais
    if a[1] == a[5] == a[9]:
        if a[1] == 'x':
            return 10
        elif a[1] == 'o':
            return -10
    if a[3] == a[5] == a[7]:
        if a[3] == 'x':
            return 10
        elif a[3] == 'o':
            return -10
    
    #Se não há vencedor
    return 0

def minimax(a, depth, is_maximizing):
    score = avaliar(a)
    
    #Se o jogador ganhou
    if score == 10:
        return score - depth
    
    #Se o CPU ganhou
    if score == -10:
        return score + depth
    
    #Se não há mais movimentos possíveis (empate)
    if not any(isinstance(v, int) for v in a.values()):
        return 0
    
    #Se é a vez do jogador
    if is_maximizing:
        best = -1000
        for i in range(1, 10):
            if isinstance(a[i], int):
                a[i] = 'x'
                best = max(best, minimax(a, depth + 1, not is_maximizing))
                a[i] = i
        return best
    #Se é a vez do CPU
    else:
        best = 1000
        for i in range(1, 10):
            if isinstance(a[i], int):
                a[i] = 'o'
                best = min(best, minimax(a, depth + 1, not is_maximizing))
                a[i] = i
        return best

def melhor_jogada_cpu(a):
    melhor_valor = 1000
    melhor_movimento = -1
    
    for i in range(1, 10):
        if isinstance(a[i], int):
            a[i] = 'o'
            movimento_valor = minimax(a, 0, True)
            a[i] = i
            if movimento_valor < melhor_valor:
                melhor_valor = movimento_valor
                melhor_movimento = i
    
    return melhor_movimento

def jogada_cpu(cpu, a):
    print()
    print('Jogada do CPU')
    melhor_movimento = melhor_jogada_cpu(a)
    a[melhor_movimento] = cpu
    cont = 1
    for i in range(3):
        print(a[cont], '|', a[cont + 1], '|', a[cont + 2])
        cont += 3
    print()
    return a


def start():
    p, c = escolha()

    a = base_do_jogo()

    print("Sorteando o primeiro jogador:")
    primeiro = randint(0, 1)

    if primeiro == 1:
        print('Você é o primeiro!')
        time.sleep(4)
        w = 0
        fim = 0
        while w == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            jogada(p, a)
            fim += 1
            w = conferir(p, a)
            if w != 0 or fim == 9:
                break
            os.system('cls' if os.name == 'nt' else 'clear')
            jogada_cpu(c, a)
            fim += 1
            w = conferir(c, a)
            if w != 0 or fim == 9:
                break
        if p == w:
            print('Você ganhou !!!')
        elif c == w:
            print('Você perdeu !!!')
        else:
            print('DEU VELHA!!!!')

    else:
        print('O CPU é o primeiro!')
        time.sleep(4)
        w = 0
        fim = 0
        while w == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            jogada_cpu(c, a)
            fim += 1
            w = conferir(c, a)
            if w != 0 or fim == 9:
                break
            os.system('cls' if os.name == 'nt' else 'clear')
            jogada(p, a)
            fim += 1
            w = conferir(p, a)
            if w != 0 or fim == 9:
                break
        if p == w:
            print('Você ganhou !!!')
        elif c == w:
            print('Você perdeu !!!')
        else:
            print('DEU VELHA!!!!')
    
    return p, a, c


if __name__ == "__main__":
    p, a, c = start()
