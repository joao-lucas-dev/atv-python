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