#Exercicio 8.4
class animal:
    def setEspecie(self, especie):
        self.esp = especie

    def setLinguagem(self, linguagem):
        self.ling = linguagem

    def fla(self):
    #exibe uma sentença pelo animal
        print('IEu sou um {} e sei {}'.format(self.esp, self.ling))

    def __init__(self, espécie='animal', linguagem='emite sons '):
        #construtor
        self.esp = espécie
        self.ling = linguagem