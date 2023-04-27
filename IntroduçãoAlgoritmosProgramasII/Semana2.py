class Point:
    #classe que representa pontos no plano
    def setx(self, coordx):
    #define coordenada x do ponto como coordx
        self.x = coordx
    def sety(self, coordy):
    #define coordenada y do ponto como coordy'
        self.y = coordy
    def get(self):
    #retorna tupla com coordenadas x e y do ponto'
        return (self.x, self.y)
    def move(self, dx, dy):
    #muda as coordenadas x e y por dx e dy
        self.x += dx
        self.y += dy

    #Exercicio 8.1
    def getx(self, coorx):
        self.x = coorx

#EXERCICIO 8.2
class teste:
    versao = 1.02

#Exercicio 8.3
class retangulo:
    def setTamanho(self, largura, comprimento):
        self.larg = largura
        self.compri = comprimento

    def setPerimetro(self, perimetro):
        self.peri =

    def setArea(self,  area):
        self.ar = self.largura * self.comprimento


#Exercicio 8.4
class animal:
    def setEspecie(self, especie):
        self.esp = especie

    def setLinguagem(self, linguagem):
        self.ling = linguagem

    def fla(self):
    #exibe uma sentença pelo animal
        print('IEu sou um {} e sei {}'.format(self.esp, self.ling))



