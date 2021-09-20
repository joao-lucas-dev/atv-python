import math

class Retangulo:

    #construtor da classe
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    #método para calcular a área
    def Area(self):
        return self.altura * self.largura

    #método para calcular o perímetro
    def Perimetro(self):
        return (2 * self.largura) + (2 * self.altura)

    #método para calcular a diagonal
    def Diagonal(self):
        return math.sqrt((self.largura**2) + (self.altura**2))


#entrada de dados
print("Insira a largura: ")
largura = float(input())
print("Insira a altura: ")
altura = float(input())

#instanciando objeto da classe Retangulo
retangulo = Retangulo(largura, altura)

#saída de dados
print("Area: " , retangulo.Area())
print("Perimetro: " , retangulo.Perimetro())
print("Diagonal: " , retangulo.Diagonal())