"""
 3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de
forma que:
 a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
 b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
 c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também
permitir que seja informado um número de canal para efetuar a troca
"""

class Televisao:

    def __init__(self):
        self.__status : bool = False
        self.__volume: int = 0
        self.__canal: int = 0

    @property
    def status(self) -> bool :
        return self.__status

    @status.setter
    def status(self, status: bool)-> None:
        self.__status = status

    @property
    def volume(self)-> int:
        return self.__volume

    @volume.setter
    def volume(self, volume: int)-> None:
        self.__volume= volume

    @property
    def canal(self)-> int:
        return self.__canal

    @canal.setter
    def status(self, canal: bool)-> None:
        self.__canal = canal

    def ligar_desligar(self)-> None:
        self.status = not self.status

        if self.status:
            print('status da tv: ligada')
        else:
            print('status da tv: desligada')


    def aumentar_volume(self)-> None:
        self.volume = self.volume + 1
        print(f'volume da tv +: {self.volume}')

    def diminuir_volume(self)-> None:
        self.volume = self.volume - 1
        print(f'volume da tv -: {self.volume}')

    def aumentar_canal(self)-> None:
        self.canal = self.canal + 1
        print(f'canal da tv +: {self.canal}')

    def diminuir_canal(self)-> None:
        self.canal = self.canal - 1
        print(f'canal da tv +: {self.canal}')

    def mudar_canal(self, canal: int) -> None:
        self.canal = canal
        print(f'canal da tv ? : {self.canal}')

class ControleRemoto:

    def __init__(self, televisao: Televisao)-> None:
        self.__televisao: Televisao = televisao

    @property
    def televisao(self)-> Televisao:
        return self.__televisao

    def ligar_desligar(self)-> None:
        self.televisao.ligar_desligar()

    def aumentar_volume(self)-> None:
        self.televisao.aumentar_volume()

    def diminuir_volume(self)-> None:
        self.televisao.diminuir_volume()

    def aumentar_canal(self)-> None:
        self.televisao.aumentar_canal()

    def diminuir_canal(self)-> None:
        self.televisao.diminuir_canal()

    def mudar_canal(self, canal: int)-> None:
        self.televisao.mudar_canal(canal)

if __name__ == '__main__':
    tv: Televisao = Televisao()

    tv.ligar_desligar()

    tv.aumentar_canal()
    tv.aumentar_canal()
    tv.aumentar_canal()

    tv.mudar_canal(42)

    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()


