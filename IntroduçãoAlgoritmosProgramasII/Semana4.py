#Exercicio 6.1
def estadoNasc(presidente):
    estado = {'Barack Hussein Obama II': 'Hawaii',
    'George Walker Bush': 'Connecticut',
    'William Jefferson Clinton': 'Arkansas',
    'George Herbert Walker Bush': 'Massachussetts',
    'Ronald Wilson Reagan': 'Illinois',
    'James Earl Carter, Jr': 'Georgia'}
    return estado[presidente]

print(estadoNasc('George Walker Bush'))

#Exercicio 6.2
def rlookup(agenda):
    numero = {'(123)456-78-90':['Anna','Karenina'],
    '(901)234-56-78':['Yu', 'Tsun'],
    '(321)908-76-54':['Hans', 'Castorp']}

    while True:
        numero = input('Digite número do telefone no formato(xxx)xxx-xx-xx: ')
        if numero in agenda:
             print(agenda[numero])
        else:
             print('O número informado não está em uso.')

    return

#Exercicio 6.4
def contaPalavra(texto):
    #exibe freq de cada palavra no texto
    listaPalavras = texto.split() # separa texto em lista de palavras
    contadores = {} # dicionário de contadores
    for palavra in listaPalavras:
        if palavra in contadores: # contador para palavra existe
            contadores[palavra] += 1
        else: # contador para palavra não existe
            contadores[palavra] = 1
    for palavra in contadores: # exibe contagens de palavras
        if contadores[palavra] == 1:
            print('{:8} aparece {} vez.'.format(palavra, contadores[palavra]))
        else:
            print('{:8} aparece {} vezes.'.format(palavra, contadores[palavra]))
    return
print(contaPalavra('Oi Mundo'))

#Exercicio 6.5
def lookup(agenda):
    #implementa serviço de agenda interativo usando o dicionário de agenda como entrada
    agenda = {('Anna', 'Karenina'): '(123)456-78-90', ('Yu', 'Tsun'): '(901)234-56-78', ('Hans', 'Castorp'):'(321)908-76-54)'}
    while True:
        nome = input('Digite o nome ')
        sobrenome = input('Digite o sobrenome ')
        pessoa = (nome, sobrenome)# constrói a chave
        if pessoa in agenda:# se a chave estiver no dicionário
            print(agenda[pessoa])# mostra o valor
        else: # se chave ausente do dicionário
            print('O nome informado não é conhecido.')

    return


#Exercicio 6.6
def sync(agendas):
    #retorna a união de conjuntos em agendas'
    res = set() # inicializa o acumulador

    for agenda in agendas:
        res = res | agenda # acumula agenda em res

    return res
agenda1 = ['4738', '9389']
agenda2 = ['02834', '9380947']
agendas = [agenda1, agenda2]
print(agendas)