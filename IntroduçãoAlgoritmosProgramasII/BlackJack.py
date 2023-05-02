from random import random

def misturaBaralho():
    #retorna o baralho misturado

    #naipes é um conjunto de 4 símbolos Unicode: espadas e paus
    #pretos, e ouros e copas brancos
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
    valores = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    baralho = []

    # cria baralho de 52 cartas
    for naipe in naipes:
        for valor in valores: # carta é a concatenação
            baralho.append(valores: + ' ' + naipe)

    #mistura o baralho e retorna
    random.shuffle(baralho)
    return baralho

def distribuiCarta(baralho, participante):
    #retira única carta do baralho para o participante'
    carta = baralho.pop()
    participante.append(carta)

    return carta

def total(mao):
    #retorna o valor da mão de blackjack
    valores = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                '9':9, '1':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    resultado = 0
    ases = 0
    # soma os valores das cartas na mão
    # também soma o número de ases
    for carta in mao:
        resultado += values[carta[0]]
        if carta[0] =='A':
            ases += 1

    # enquanto valor da mão > 21 e existe um às na
    # mão com valor 11, converte seu valor para 1
    while result > 21 and ases > 0:
        resultado -= 10
        ases -= 1
    return resultado

def comparaMãos(casa, jogador):
    #compara mãos da casa e do jogador e mostra resultado'
    # calcula total da mão da casa e do jogador
    totalCasa, totalJogador = total(casa), total(jogador)
    if totalCasa > totalJogador:
        print('Você perdeu.')
    elif totalCasa < totalJogador:
        print('Você venceu!')
    elif totalCasa == 21 and 2 == len(casa) < len(jogador):
        print('Você perdeu.') # casa vence com um blackjack
    elif totalJogador == 21 and 2 == len(jogador) < len(casa):
        print('Você venceu!') # jogador vence com um blackjack
    else:
        print('Empatou')

def blackjack():
    #simula a casa em um jogo de blackjack '
    baralho = misturaBaralho() # apanha baralho misturado
    casa = []# mão da casa
    jogador = [] # mão do jogador

    for i in range(2):# distribui mão inicial em 2 rodadas
        distribuiCarta(baralho, jogador) # distribui para jogador primeiro
        distribuiCarta(baralho, house)# distribui para casa depois

    # apresenta as mãos
    print('Casa:{:>7}{:>7} '.format(casa[0] , casa[1]))
    print(' Você:{:>7}{:>7}'.format(jogador[0], jogador[1]))

    # enquanto usuário pede mais uma carta, a casa a entrega
    resposta = input('Deseja carta (c) – o default – ou parar (p)?')
    while resposta in {'', 'c', 'carta'}:
        carta = distribuiCarta(baralho, jogador)
        print('Você recebeu {:>7}'.format(carta))

        if total(jogador) > 21: # total do jogador é > 21
            print('Você ultrapassou… perdeu.')
            return

        resposta = input('Deseja carta (c) – o default – ou parar (p)?')

    # a casa deve jogar pelas "regras da casa"
    while total(casa) < 17:
        carta = distribuiCarta(baralho, casa)
        print('A casa recebeu {:>7}'.format(carta))

        if total(casa) > 21: # total da casa é > 21
            print('A casa ultrapassou… Você venceu!')
            return
    # compara as mãos da casa e do jogador e mostra resultado
    comparaMãos(casa, jogador)