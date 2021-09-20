'''Ler nome e salário de dois funcionários, mostrar o salário médio dos funcionários'''

class Funcionarios:

    def __init__(self, sum_salarios, media_salarial):
        self.sum_salarios = sum_salarios
        self.media_salarial = media_salarial

    def mediaSalarial(self):
        self.sum_salarios = sum([salario_01, salario_02])
        self.media_salarial = self.sum_salarios/2

        return self.media_salarial

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
