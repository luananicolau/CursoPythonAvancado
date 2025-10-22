"""3. Crie um programa, instancie um objeto da classe Carro e teste o seu médodo
"""

from exercicio2 import Carro

if __name__ == '__main__':
    carro: Carro = Carro(marca= 'Honda', modelo='fiat', portas=4)

    carro.imprimir()