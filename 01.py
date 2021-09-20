
"""Q01-Ler os dados de duas pessoas, mostrar o nome da pessoa mais velha."""

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
