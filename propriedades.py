"""
POO - propriedades - properties

Em lingaugens de programação como o Java, ao declararmos atributos privados nas classes, costumamos
a criar  métodos públicos para manipulação desses atributos. Esses métodos são conhecidos por getters e setters,
onde os getters retornam o valor do atributo e os setters alteram o valor do mesmo.

Consultar atributos - getters

consultar E ALTERAR atributos - setters
"""
class ContaCorrente:
    contador = 4999

    def __init__(self, titular, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__titular = titular
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = ContaCorrente("luana", 3000, 2300)
conta2 = ContaCorrente("jose", 2000, 1000)

print(conta1.extrato())
print(conta2.extrato())

print(conta1.saldo)  # Uso do getter do saldo

conta1.saldo = 9999999  # Uso do setter

print(conta1.saldo)
