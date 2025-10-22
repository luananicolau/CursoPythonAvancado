"""
1. Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe
"""

class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self) -> str:
        return self.__marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @marca.setter
    def marca(self, nova_marca: str) -> None:
        self.__marca = nova_marca

    @modelo.setter
    def modelo(self, nova_modelo: str) -> None:
        self.__modelo = nova_modelo

    def dados_veiculo(self) -> None:
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

