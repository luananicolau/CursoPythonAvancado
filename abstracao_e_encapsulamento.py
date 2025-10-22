"""
POO - abstração e encapsulamento

O grande objetivo é encapsular nosso codigi dentro de um grupo logico e hierarquico utilizando classes

encapsular -> capsula

abstração, em poo, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos emétodos privados de usuário.


"""
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


# testando
conta1 = Conta('Luana', 150.00, 2000)

print(conta1.__dict__)  # mostra os atributos internos

conta1.extrato()  # exibe o extrato

print(conta1._Conta__titular)  # acessando atributo privado via name mangling



