#Excicio 2.1
# A soma dos 5 primeiros inteiros positivos.
soma = (1 + 2 + 3 + 4 + 5)
print(soma)

# A idade média de Sara (idade 65), Fátima (idade 56) e Mark (idade 45)
sara = 65
fatima = 56
mark = 45
media = (sara + fatima + mark) / 3
print(media)

#2 à 10 potência
potencia = 2**10
print(potencia)

# O número de vezes que 73 cabe em 403.
divisao = 403 // 73

# O resto de quando 403 é dividido por 73.
resto = 403 % 37
print(resto)

# O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
absoluto = (sara - mark)
print(absoluto)

# O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
preco1 = 34.99
preco2 = 29.95
preco3 = 31.50
print(min(preco1, preco2, preco3))

# Exercicio 2.2
# A soma de 2 e 2 é menor que 4
res = 2 + 2 < 4
print(res)

# O valor de 7 // 3 é igual a 1 + 1.
res1 = 7 // 3 == 1 + 1
print(res1)

# A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
res3 = 3**2 + 4**2 == 25
print(res3)

# A soma de 2, 4 e 6 é maior que 12.
res4 = 2 + 4 + 6 > 12
print(res4)

# 1387 é divisível por 19.
res8 = 1387 % 19 == 0
print(res8)

# 31 é par.
res5 = 31 % 2 == 0
print(res5)

# O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.
res6 = min(preco1, preco2, preco3) < 30.00
print(res6)

# Exercicio 2.3
# Atribua o valor inteiro 3 à variável a.
a = 3

# Atribua 4 à variável b.
b = 4

# Atribua à variável c o valor da expressão a * a + b * b.
c = a * a + b * b
print(c)

# Exercicio 2.4
s1 = 'ant '
s2 = 'bat '
s3 = 'cod '
# 'ant bat cod'
print(s1 + s2 + s3)

# ant ant ant ant ant ant ant ant ant ant
print(s1 * 10)

# 'ant bat bat cod cod cod'
print(s1 + s2 * 2 + s3 * 3)

# ant bat ant bat ant bat ant bat ant bat ant bat ant bat
print((s1 + s2) * 7)

# batbatcod batbatcod batbatcod batbatcod batbatcod
print((s2 + s2 + s3) * 5)

# Exercicio 2.5
s = '0123456789'
print(s[0])
print(s[1])
print(s[6])
print(s[8])
print(s[9])