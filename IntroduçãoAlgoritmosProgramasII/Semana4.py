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
        numero = input('Digite número do telefone no formato(xxx) xxx - xx - xx: ')
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

