from random import randint

def escolha():
    p = 999
    print('Escolha com qual caractere vai jogar.')
    while p != 'x' and p!= 'o':
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
    return p,c


def base_do_jogo():
    a = dict()
    cont = 1
    for i in range(9):
        a[cont] = cont
        cont += 1
    return a


def jogada(player,a):
    while True:
        print('Faça sua jogada escolhendo as posições disponíveis')
        cont = 1
        for i in range(3):
            print(a[cont] , '|' , a[cont + 1] , '|' , a[cont + 2])
            cont += 3        
        joga = input('Digite um número de 1 a 9: ')
        if joga != '1' and joga !='2' and joga != '3' and joga != '4' and joga != '5' and joga != '6' and joga != '7' and joga != '8' and joga != '9': 
            print()
            continue
        else:
            joga = int(joga)
            if a[joga] == 'x' or a[joga] == 'o':
                print('O campo já foi escolhido')
                continue
            a[joga] = player
            cont = 1
            for i in range(3):
                print(a[cont] , '|' , a[cont + 1] , '|' , a[cont + 2])
                cont += 3
            break
        print()
        return a
        

def conferir(player,a):
    #linha
    w=0
    if a[1] == player and a[2] == player and a[3] == player:
        w = player
        
    if a[4] == player and a[5] == player and a[6] == player:
        w = player
        
    if a[7] == player and a[8] == player and a[9] == player:
        w = player
        
    #coluna
    if a[1] == player and a[4] == player and a[7] == player:
        w = player
        
    if a[2] == player and a[5] == player and a[8] == player:
        w = player
        
    if a[3] == player and a[6] == player and a[9] == player:
        w = player
        
    #diagonais
    if a[1] == player and a[5] == player and a[9] == player:
        w = player
        
    if a[3] == player and a[5] == player and a[7] == player:
        w = player
    
    
    if w != 0:
        return player
    if w == 0:
        return 0
    

# cpu em implementação, será retirada a jogada aleatória para uma mais inteligente.
def jogada_cpu(cpu,a):
    print()
    print('Jogada do CPU')
    while True:
        joga = randint(1,9)
        if a[joga] == 'x' or a[joga] == 'o':
            #print('O campo já foi escolhido')
            continue
        a[joga] = cpu
        cont = 1
        for i in range(3):
            print(a[cont] , '|' , a[cont + 1] , '|' , a[cont + 2])
            cont += 3
        break
    print()
        
    return a


    

def start():
    p,c = escolha()

    a = base_do_jogo()

    print("Sorteando o primeiro jogador:")
    primeiro = randint(0,1)

    if primeiro == 1:
        print('Você é o primeiro!')
        w = 0
        fim = 0
        while w == 0:
            jogada(p,a)
            fim += 1
            w = conferir(p,a)
            if w != 0 or fim == 9:
                break
            jogada_cpu(c,a)
            fim += 1
            w = conferir(c,a)
            if w != 0 or fim == 9:
                break
        if p == w:
            print('Você ganhou !!!')
        if c == w:
            print('Você perdeu !!!')
        if fim == 9:
            print('DEU VELHA!!!!')




    else:
        print('O CPU é o primeiro!')
        w = 0
        fim = 0
        while w == 0:
            
            jogada_cpu(c,a)
            fim += 1
            w = conferir(c,a)
            if w != 0 or fim == 9:
                break
            jogada(p,a)
            fim += 1
            w = conferir(p,a)
            if w != 0 or fim == 9:
                break
        if p == w:
            print('Você ganhou !!!')
        if c == w:
            print('Você perdeu !!!')
        if fim == 9:
            print('DEU VELHA!!!!')
    
    
    return p,a,c


p,a,c=start()




    
