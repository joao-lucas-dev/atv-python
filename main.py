import math

#classe da questão 1
class Pessoas:

    def __init__(self, maior, pessoa_mais):
        self.maior = maior
        self.pessoa_mais = pessoa_mais

    def maisVelha(self):
        list_idades = [idade_01, idade_02]
        self.maior = max(list_idades)

        #verificando a mais velha
        if(idade_01 == idade_02):
            self.pessoa_mais = f'{nome_01} e {nome_02} tem idades iguais.'
        elif(self.maior == idade_01):
            self.pessoa_mais = nome_01
        elif(self.maior == idade_02):
            self.pessoa_mais = nome_02
        return self.pessoa_mais

#classe da questão 2
class Funcionarios:

    def __init__(self, sum_salarios, media_salarial):
        self.sum_salarios = sum_salarios
        self.media_salarial = media_salarial

    def mediaSalarial(self):
        self.sum_salarios = sum([salario_01, salario_02])
        self.media_salarial = self.sum_salarios/2

        return self.media_salarial



#classe da questão 3
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

#classe da questão 4
class Funcionario:

    #construtor
    def __init__(self, nome, salarioBruto, imposto):
        self.nome = nome
        self.salarioBruto = salarioBruto
        self.imposto = imposto

    #método para calcular o salário líquido
    def SalarioLiquido(self):
        return float(self.salarioBruto - self.imposto)

    #método para aumentar o salário bruto com a porcentagem
    def AumentarSalario(self, porcentagem):
        self.salarioBruto = self.salarioBruto +  (self.salarioBruto * porcentagem/100)

#classe para a questão 5
class Aluno: 

    def __init__(self, nota_final):
        self.nota_final = nota_final

    def resultado(self):
        list_notas = [nota_01, nota_02, nota_03]
        self.nota_final = sum(list_notas)

        print(f'NOTA FINAL = {self.nota_final}')
        print
        if(self.nota_final < 60.00):
            pontos = 60 - self.nota_final 
            result = f'REPROVADO(A)\nFALTARAM {pontos} PONTOS.'
        elif(self.nota_final >= 60):
            result = f'APROVADO'
        return result


#classe main para o menu
class Main:

    def __init__(self, questoes):
        self.questoes = questoes 


print("Escolha a questão:  \n 1 - Questão 1 \n 2 - Questão 2 \n 3 - Questão 3 \n 4 - Questão 4 \n 5 - Questão 5 \n Escolha:")
escolha = int(input())

if escolha == 1:
    #Dados da primeira pessoa
    print('Dados da primeira pessoa: ')
    nome_01 = input('Nome: ')
    idade_01 = int(input('Idade: '))

    #Dados da segunda pessoa
    print('Dados da segunda pessoa: ')
    nome_02 = input('Nome: ')
    idade_02 = int(input('Idade: '))

    pessoas = Pessoas(None, None)

    #saída de dados
    print(f'Pessoa mais velha: {pessoas.maisVelha()}')

elif escolha == 2:
    #Dados funcionário 01:
    print('Dados do primeiro funcionário: ')
    nome_01 = input('Nome: ')
    salario_01 = float(input('Salário: '))

    #Dados funcionário 02:
    print('Dados do segundo funcionário: ')
    nome_02 = input('Nome: ')
    salario_02 = float(input('Salário: '))

    funcionarios = Funcionarios(None, None)

    print(f'Salário médio = {funcionarios.mediaSalarial()}')

elif escolha == 3: 
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

elif escolha == 4:
    #entrada de dados
    print("Nome: ")
    nome = input()
    print("Salário bruto: ")
    salarioBruto = float(input())
    print("Imposto: ")
    imposto = float(input())

    #instanciando objeto da classe Funcionário
    funcionario = Funcionario(nome, salarioBruto, imposto)

    #saída de dados originais
    print("Funcionário: ", funcionario.nome, ", R$ ", funcionario.SalarioLiquido())

    print("Digite a porcentagem para aumentar o salário: ")
    porcentagem = float(input())

    funcionario.AumentarSalario(porcentagem)

    #saída de dados
    print("Dados atualizados: ", funcionario.nome, ", R$ ", funcionario.SalarioLiquido())

elif escolha == 5:
    nome = input('Nome do Aluno: ')
    nota_01 = float(input('Digite as três notas do aluno: '))
    nota_02 = float(input('\t\t\t       '))
    nota_03 = float(input('\t\t\t       '))

    aluno = Aluno(None)
    print(f'{aluno.resultado()}')

else: 
    print("Insira uma escolha válida")