#Exercicio 3.14
def trocaPU(lst):
    lst[0], lst[-1] = lst[-1], lst[0]

    return
ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
trocaPU(ingredientes)
print(ingredientes)

#Exercicio 3.15
import turtlefunctions
def olimpiadas(t):
#faz tartaruga t desenhar os anéis olímpia
    t.pensize(3)
    turtlefunctions.jump(t, 0, 0) # fundo do círculo superior central
    t.setheading(0)
    t.circle(100) # círculo superior central
    turtlefunctions.jump(t, -220, 0)
    t.circle(100) # círculo superior esquerdo
    turtlefunctions.jump(t, 220, 0)
    t.circle(100) # círculo superior direito
    turtlefunctions.jump(t, 110, -100)
    t.circle(100) # círculo inferior direito
    turtlefunctions.jump(t, -110, -100)
    t.circle(100) # círculo inferior esquerdo
    return

import turtle
s = turtle.Screen()
t = turtle.Turtle()
olimpiadas(t)

#Exercicio 4.8
def palavras(nomeArq):
#retorna a lista de palavras reais, sem pontos
    arqEntrada = open('Telefone-20-04.txt', 'r')
    conteúdo = arqEntrada.read()
    arqEntrada.close()
    tabela = str.maketrans('!,.:;?', 6*' ')
    conteúdo=conteúdo.translate(tabela)
    conteúdo=conteúdo.lower()
    return conteúdo.split()

print(palavras)

#Exercicio 4.9
def meuGrep(nomeArq, alvo):
#exibe cada linha do arquivo que contém a string alvo
    arqEntrada = open('Telefone-20-04.txt')
    for linha in arqEntrada:
        if alvo in linha:
            print(linha, end='')

    return linha.split()
