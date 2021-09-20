'''Ler nome e salário de dois funcionários, mostrar o salário médio dos funcionários'''

class Funcionarios:
    #Dados funcionário 01:
    print('Dados do primeiro funcionário: ')
    nome_01 = input('Nome: ')
    salario_01 = float(input('Salário: '))

    #Dados funcionário 02:
    print('Dados do segundo funcionário: ')
    nome_02 = input('Nome: ')
    salario_02 = float(input('Salário: '))

    sum_salarios = sum([salario_01, salario_02])

    media_salarial = sum_salarios/2

    print(f'Salário médio = {media_salarial}')

