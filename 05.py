'''Ler o nome do aluno e suas três notas
primeiro trimestre nota máxima: 30
segundo trimestre e terceiro nota máxima: 35 
mostrar a nota final do aluno no ano, para ser aprovado é preciso ter 60 pontos no minímo
APROVADO  ou REPROVADO?
se reprovado, pontuação que falta para o aluno ser APROVADO'''

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

nome = input('Nome do Aluno: ')
nota_01 = float(input('Digite as três notas do aluno: '))
nota_02 = float(input('\t\t\t       '))
nota_03 = float(input('\t\t\t       '))

aluno = Aluno(None)
print(f'{aluno.resultado()}')
