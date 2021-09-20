
"""Q01-Ler os dados de duas pessoas, mostrar o nome da pessoa mais velha."""

class Pessoas:
    #Dados da primeira pessoa
    print('Dados da primeira pessoa: ')
    nome_01 = input('Nome: ')
    idade_01 = int(input('Idade: '))

    #Dados da segunda pessoa
    print('Dados da segunda pessoa: ')
    nome_02 = input('Nome: ')
    idade_02 = int(input('Idade: '))

    list_idades = [idade_01, idade_02]
    maior = max(list_idades)

    #verificando a mais velha
    if(idade_01 == idade_02):
        print(f'{nome_01} e {nome_02} tem idades iguais.')
    elif(maior == idade_01):
        print(f'Pessoa mais velha {nome_01}')
    elif(maior == idade_02):
        print(f'Pessoa mais velha: {nome_02}')


