# Exercício 3.2
# Traduza estas instruções condicionais em instruções if do Python:
# (a) Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'
idade = eval(input("Digite a sua idade:"))
if idade > 62:
    print("Você pode obter benefícios de pensão")
print("Você não pode receber pensão")

# (b) Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
# exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.
nome = input('Digite um nome de jogador de beisebol:')
if nome in ["Musial", "Aaraon", "Williams", "Gehrig", "Ruth"]:
    print("Um dos 5 maiores jogadores de beisebol de todos os tempos!")
else:
    print("Esse jogador não é uns dos 5 melhores de todos os tempos!")

# (c) Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
golpes = eval(input("Digite o valor do Golpe:"))
defesa = eval(input("Digite o valor da defesa:"))
if golpes >= 10 and defesa == 0:
    print("Você está morto...")
else:
    print("Você não morreu!")

# (d) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.
norte = input("Norte é verdadeiro ou falso:")
sul = input("Sul é verdadeiro ou falso:")
leste = input("Leste é verdadeiro ou falso:")
oeste = input("Oeste é verdadeiro ou falso:")
if norte or sul or leste or oeste:
    print("Posso escapar.")
else:
    print("Não pode escapar")

# Exercício 3.3
# Traduza estas declarações em instruções if/else do Python:
# (a) Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.
#  caso contrário, exiba 'Definitivamente não é um ano bissexto.'
ano = eval(input("Digite o ano:"))
if ano % 4 == 0:
    print("Pode ser um ano bissexto.")
else:
    print("Definitivamente não é um ano bissexto.")

# (b) Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!';
# se não, exiba 'Melhor sorte da próxima vez...
bilhete = []
loteria = [5, 6, 60, 20, 46, 38]
for i in range(6):
    bilhete = eval(input("Digite os números que você vai jogar:"))

if bilhete in loteria:
    print("Você ganhou!")
else:
    print("Melhor sorte da próxima vez...")

# Exercício 3.4
# Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string).
# O programa, então, verifica se a identificação informada pelo usuário está na lista
# ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos. Dependendo do resultado,
# uma mensagem apropriada deverá ser impressa. Não importando o resultado, sua função deverá exibir 'Fim.'antes de terminar
lista = ["joe", "sue", "hani", "sophie"]
login = input("Digite o Usuáro:")
if login in lista:
    print("Você entrou!")
else:
    print("Usuário desconhecido.")
print("Fim!")

# Exercício 5.1
# Implemente a função meuIMC(), que aceita como entrada a altura de uma pessoa (em metros) e o peso (em quilos)
# e calcula o Índice de Massa Corporal (IMC) dessa pessoa. A fórmula do IMC é:
def meuIMC(peso, altura):
    imc = peso / (altura * altura)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25.0:
        print("Normal")
    elif imc >= 25.0:
        print("Sobrepeso")
    print("Seu IMC é:", imc)
    return

meuIMC(peso = eval(input("Digite o seu peso:")), altura = eval(input("Digite a sua altura:")))
