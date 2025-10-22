"""
Method Resolution Order - é a ordem de execução dos métodos, ou seja, quem vai ser executado primeiro

Em Python, podemos conferir a ordem de execução do métdo de tres formas:
- via proprieddde da classe
- via método (mro)
- via help
"""


class SerVivo:
    def mover(self):
        print("SerVivo: me movo de alguma forma.")


class Terrestre(SerVivo):
    def mover(self):
        print("Terrestre: ando com as pernas.")


class Aquatico(SerVivo):
    def mover(self):
        print("Aquatico: nado com nadadeiras.")


class Sapo(Terrestre, Aquatico):  # Essa ordem importa para o MRO
    pass


s = Sapo()
s.mover()
print(Sapo.__mro__)