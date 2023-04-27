# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
# A fórmula de conversão é F ← C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
celcius = int(input("Digite a temperatura em graus Celcius: "))
fahren = celcius * 9 / 5 + 32
print("A temperatura em Fahrenheit é : " , fahren)

#Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
#representadas pelas variáveis N1, N2, N3 e N4.
#Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média”
#se a média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno Reprovado com média”.
#Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.
n1 = int(input("Digite a primeira nota : "))
n2 = int(input("Digite a segunda nota : "))
n3 = int(input("Digite a terceira nota : "))
n4 = int(input("Digite a quarta nota : "))
media = (n1 + n2 + n3 + n4) / 4
print("Sua média foi: ", media)
if(media >= 5):
    print("Aluno aprovado!")
else:
    print("Aluno Reprovado!!")

#Desenvolver os diagramas de blocos e as codificações em português estruturado usando laço incondicional
# (para) do seguinte problema: Construir um programa que apresente a soma dos cem primeiros
# números naturais (1 + 2 + 3 +...+ 98 + 99 + 100).
soma = 0
for i in range(1, 101):
    soma+= i

print("O resultado da soma é", soma)


