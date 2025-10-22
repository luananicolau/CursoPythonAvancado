"""
Métodos mágicos são todos os métodos que utilizam dunder

dunder init -> __init__()

Dunder > Double Underscore

"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"Nome completo: {self.__nome} {self.__sobrenome}"

    def __str__(self):
        return self.__nome

    def __repr__(self):
        return f"{self.__nome}, {self.__cpf}"


pess1 = Pessoa("luana", "nicolau", "123.456.678-91")

print(pess1)