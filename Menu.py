import py_compile
class Menu:
    def __init__(self, escolha):
        self.escolha = escolha

    def menu():
        while opcao != 5:
            print('''
                    MENU:

                    [1] - Questão 01
                    [2] - Questão 02
                    [3] - Questão 03
                    [4] - Questão 04
                    [5] - Questão 05
                    [0] - Sair
                ''')

    def opcao(self):
        if self.escolha == '0':
            print('Finalizando o programa...')
            exit()
        elif self.escolha == '1':
            resposta = py_compile.compile("01.py")
        elif self.escolha == '2':
            resposta = resposta = py_compile.compile("02.py")
        elif self.escolha == '3':
            resposta = resposta = py_compile.compile("03.py")
        elif self.escolha == '4':
            resposta = resposta = py_compile.compile("04.py")
        elif self.escolha == '5':
            resposta = resposta = py_compile.compile("05.py")
        return resposta

opcao = 0
menu = Menu(None)
print(menu.menu())
print(menu.opcao())


