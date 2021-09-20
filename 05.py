'''Ler o nome do aluno e suas três notas
primeiro trimestre nota máxima: 30
segundo trimestre e terceiro nota máxima: 35 
mostrar a nota final do aluno no ano, para ser aprovado é preciso ter 60 pontos no minímo
APROVADO  ou REPROVADO?
se reprovado, pontuação que falta para o aluno ser APROVADO'''

class Aluno: 
    nome = input('Nome do Aluno: ')
    nota_01 = float(input('Digite as três notas do aluno: '))
    nota_02 = float(input('\t\t\t       '))
    nota_03 = float(input('\t\t\t       '))

    nota_final = sum([nota_01, nota_02, nota_03])

    print(f'NOTA FINAL = {nota_final}')

    if(nota_final < 60.00):
        pontos = 60 - nota_final 
        print(f'REPROVADO\nFALTARAM {pontos} PONTOS.')
    elif(nota_final >= 60):
        print(f'APROVADO')