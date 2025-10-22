"""
POO - objetos

Objetos são instancias da classe.
"""
from dicionarios import usuario


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

lamp1 = Lampada('branca', 110, 60)


# objetos / instancias

lamp1.ligar_desligar()


print(f'a lampada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 2000)

user1 = Usuario('luana', 'nicolau', 'luananicolau@gmail.com', '070707')
