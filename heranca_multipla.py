"""
POO- herança multipla


"""

class Mamifero:
    def amamentar(self):
        print("Sou mamífero e amamento.")


class Aquatico:
    def nadar(self):
        print("Sou aquático e sei nadar.")


# Herança múltipla direta
class Golfinho(Mamifero, Aquatico):
    pass


g = Golfinho()
g.amamentar()
g.nadar()


class SerVivo:
    def respirar(self):
        print("Respiro oxigênio.")


class Terrestre(SerVivo):
    def andar(self):
        print("Ando sobre a terra.")


class Aquatico(SerVivo):
    def nadar(self):
        print("Nado na água.")


# Herança múltipla indireta
class Sapo(Terrestre, Aquatico):
    def coaxar(self):
        print("Coaxo ribbit!")


s = Sapo()
s.respirar()  # Herdado indiretamente de SerVivo
s.andar()  # De Terrestre
s.nadar()  # De Aquatico
s.coaxar()  # Da própria classe


# Descobrir se objeto é instância de
print(f"'s' é instância de Aquatico? {isinstance(s, Aquatico)}")
print(f"'s' é instância de Terrestre? {isinstance(s, Terrestre)}")
print(f"'s' é instância de SerVivo? {isinstance(s, SerVivo)}")
print(f"'s' é instância de Golfinho? {isinstance(s, Golfinho)}")
print(f"'s' é instância de object? {isinstance(s, object)}")  # Todo objeto é