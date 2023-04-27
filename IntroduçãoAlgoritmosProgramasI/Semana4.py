# Exercício 3.1
# Implemente um programa que solicita a temperatura atual
# em graus Fahrenheit do usuário e exibe a temperatura em graus Celsius usando a fórmula 5 / 9 (Fahrenheit - 32)
import math

fahrenheit = eval(input("Digite a temperatura em Fahrenheit:"))
celcius =(fahrenheit - 32) *  5 / 9
print("Temperatura em celcius é", celcius)

# Exercício 3.8
# Defina, diretamente no shell interativo, a função média(),
# que aceita dois números como entrada e retorna a média dos números. Um exemplo de uso é:
def media(x, y):

    return (x +y) / 2
print("A média da nota é:", media(x = eval(input("Digite a 1° nota:")), y = eval(input("Digite a 2° nota: "))))

# Exercício 3.9
# Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo (um número não negativo)
# e retorna o perímetro do círculo.
def perimetro(raio):

    return 2 *math.pi * raio
print("O perimetro é ", perimetro(eval(input("Digite o valor do raio:"))))

# Exercício 3.10
# Escreva a função negativos(), que aceita uma lista como entrada e exibe,
# um por linha, os valores negativos na lista. A função não deverá retornar nada.
def negativos(lista):
    for i in lista:
        if i < 0:
            print(i)
    return

# Exercício 3.13
# Suponha que uma lista não vazia time foi atribuída. Escreva uma instrução Python
# ou instruções que mapeiam o primeiro e último valor da lista. Assim, se a lista original for:
time = ["Ava", "Eleanor", "Clare", "Sarah"]
time[0], time[-1] = time[-1], time[0]

print(time)

# Exercício 3.14
# Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista.
# Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.
def trocaPU(lst):

    return
ingredientes = ["farinha", "açúcar", "manteiga", "maçãs"]
trocaPU(ingredientes)
ingredientes[0], ingredientes[-1] = ingredientes[-1], ingredientes[0]
print(ingredientes)





