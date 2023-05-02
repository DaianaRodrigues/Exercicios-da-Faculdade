from random import shuffle

class Baralho:
    #representa um baralho de 52 cartas'

    # valores e naipes são variáveis da classe Baralho
    valores = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    # naipes são 4 símbolos Unicode representando os 4 naipes
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self, listaCartas=None):
    #inicializa baralho de 52 cartas'
        self.baralho = [] # baralho está inicialmente vazio

        if listaCartas != None:# entra baralho fornecido
            self.baralho = listaCartas
        else: # nenhum baralho incluído
            #self.baralho é uma lista de 52 cartas de jogo
            for naipe in Baralho.naipes: # naipes e valores são Baralho
                for valor in Baralho.valores: # variáveis da classe
                    #inclui Carta com certo valor e naipe no baralho
                    self.baralho.append(Carta(valor, naipe))

    def distribuiCarta(self):
        #distribui (remove e retorna) carta do topo do baralho'
        return self.baralho.pop()

    def shuffle(self):
        #mistura o baralho'
        shuffle(self.baralho)

    def __repr__(self):
    #retorna representação formal'
        return "Carta('{}', '{}')".format(self.valor, self.naipe)

    def __eq__(self, outro):
    #self = outro se valor e naipe forem os mesmos'
        return self.valor == outro.valor and self.naipe == outro.naipe

    def __len__(self):
    #retorna tamanho do baralho'
        return len(self.baralho)

    def __repr__(self):
    #retorna representação de string canônica'
        return 'Baralho ({})'.format(self.baralho)

    def __eq__(self, outro):
    #retorna True se baralho tiver as mesmas cartas na mesma ordem
        return self.baralho == outro.baralho