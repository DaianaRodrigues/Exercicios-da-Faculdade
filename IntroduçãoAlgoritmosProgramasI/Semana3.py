# Exercício 2.6
#escreva duas expressões Python que são avaliadas,
#respectivamente, como a primeiro e a última palavras em palavras, na ordem do dicionário.
import math
from itertools import count

palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
print(sorted(palavras[0]))
print(sorted(palavras[4]))

# Exercício 2.7
# Dada a lista de notas de trabalho de casa dos alunos
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# (a) Uma expressão que avalia para o número de 7 notas.
print(notas.count(7))

# (b) Uma instrução que muda a última nota para 4.
notas[-1] = 4
print(notas)

# (c) Uma expressão que avalia para a nota mais alta.
print(max(notas))

# (d) Uma instrução que classifica as notas da lista.
print(notas.sort())

# (e) Uma expressão que avalia para a média das notas.
media = sum(notas) / len(notas)
print("A média das notas são:", media)

# Exercício 2.8
# Em que ordem os operadores nas expressões a seguir são avaliados?
# (a) 2 + 3 == 4 or a >= 5
# (b) lst[1] * -3 < -10 == 0
# (c) (lst[1] * -3 < -10) in [0, True]
# (d) 2 * 3**2
# (e) 4 / 2 in [1, 2, 3]

#A ordem é indicada por meio de parêntes
# (a)((2 + 3) == 4) or (a >= 5)
# (b)(((lst[1]) * (-3)) < (-10)) == 0
# (c)(((lst[1]) * (-3)) < (-10)) in [0, True]
# (d)2 * (3**2)
# (e)(4 / 2) in [1, 2, 3]

# Exercício 2.9
# Qual é o tipo do objeto ao qual essas expressões são avaliadas?
print(False + False)
print(2 * 3**2.0)
print(4 // 2 + 4 % 2)
print(2 + 3 == 4 or 5 >= 5)

# Exercício 2.10
# Escreva expressões Python correspondentes ao seguinte:
# (a) O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
a = eval(input("Digite o valor do lado a do triangulo: "))
b = eval(input("Digite o valor do lado b do triangulo:"))
resul = math.sqrt(a**2 + b**2)

# (b) O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
if(resul >= 5):
    print("O valor do comprimento da Hipotenusa é: ", resul)
else:
    print("O valor do comprimento da Hipotenusa é menor que 5")

# (c) A área de um disco com raio a
r = eval(input("Digite o valor do raio: "))
area = math.pi * r**2
print("Area do disco tem o tamanho:", area)

# (d) O valor da expressão Booleana que verifica se um ponto com coordenadas x e y
# está dentro de um círculo com centro ( a, b ) e raio r
x = eval(input("Digite o valor da 1° coordenada:"))
y = eval(input("Digite o valor da 2° coordenada:"))

if((x - a)**2 + (y - b)**2 < r**2):
    print("A coordenada está dentro do valor do circulo e do raio!")
else:
    print("A coordenada não está dentro do valor do circulo e do raio!")


