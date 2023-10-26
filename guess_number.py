import time
import random

print(':::...Iniciando o Jogo de Adivinhação...:::')
time.sleep(2)
print('Escolha a dificuldade desejada!')
time.sleep(2)
print('Nível de dificuldade: Facil, Médio ou Difícil!')
time.sleep(2)
escolheu_nível = False

while escolheu_nível == False:
    print("Escolha um Nível!")
    dificuldade = input('Digite 1(fácil), 2(médio) ou 3(díficil): ')
    try: 
        dificuldade = int(dificuldade)
    except:
        print('Digite um dos números: 1, 2 ou 3')
        pass
    niveis = (1, 2, 3)

    if dificuldade in niveis:
        if dificuldade == 1:
            level = 1
            escolheu_nível = True
            print('Você escolheu o nível Fácil, tem 10 tentativas')
        elif dificuldade == 2:
            level = 2
            escolheu_nível = True
            print('Você escolheu o nível Fácil, tem 5 tentativas')
        else:
            level = 3
            escolheu_nível = True
            print('Você escolheu o nível Fácil, tem 3 tentativas')
    else:
        print('Digite um dos números: 1, 2 ou 3')
        escolheu_nível = False

# Determinado o número de chances que o jogador terá
if level == 1:
    chances = 20
elif level == 2:
    chances = 10
else:
    chances = 5

number = random.randint(1, 100)# Numéro definido pelo programa, deve ser adivinhado pelo usuário

a = 1 

while a <= chances:
    print(f'Você está na rodada {a}')

    # Esse pedaço de código recebe o número a cada tentativa, caso não seja um número valido, enviará um aviso e reiniciará a rodada
    num = input('Escolha um número de 1 a 100!')
    try:
        num = int(num)
    except:
        print('Escolha um número válido')
        pass

    ### Verificando se acertou o número 

    if num == number:
        print(f'Parabéns Você Acertou!! o número secreto é {number}')
        break
    else:
        if num > number:
            print('O número escolhido é maior que o número secreto!!')
        elif num < number:
            print('O número escolhido é menor que o número secreto!!')

    restam = chances - a
    print(f'Restam {restam} chances!!!')
    a += 1

print('Fim de Jogo, Você não Acertou o número secreto!')

