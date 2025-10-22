"""
Poli -> Muitas
Morfis -> Formas

objetos que podem se comportar de muitas formas
"""

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar esse método")

    def comer(self):
        print(f"{self.__nome} está comento...")


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self.__nome} fala auau")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala miau")


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala llllll")


felix = Gato("Felix")
felix.comer()
felix.falar()

feio = Rato("Jerry")
feio.falar()