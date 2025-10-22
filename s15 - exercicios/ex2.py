"""
 2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
 a) armazenar_contato(contato: Contato);
 b) remover_contato(contato: Contato);
 c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
 d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
 e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""

from datetime import date

from ex1 import Pessoa

class Agenda:

    def __init__(self):
        self.__contatos = list[Pessoa] = []

    @property
    def contatos(self)-> list[Pessoa]:
        return self.__contatos

    def armazenar_contato(self, contato: Pessoa)-> None:
            self.contatos.append(contato)

    def remover_contato(self, contato: Pessoa)-> None:
            self.contatos.remove(contato)

    def buscar_contato(self, nome: str) -> None:
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'o contato {nome} esta na posicao {indice}')

    def imprimir_agenda(self) -> None:
        for contato in self.contatos:
            contato.imprimir()

    def imprimir_contato(self, indice: int) -> None:
        self.contatos[indice].imprimir()

if __name__ == '__main__':
    contato1: Pessoa = Pessoa('luana', date(2006, 7, 7), 'luana@email.com')
    contato2: Pessoa = Pessoa('raissa', date(2006, 7, 7), 'raissa@email.com')
    contato3: Pessoa = Pessoa('ana paula', date(2006, 7, 7), 'anapaula@email.com')

    agenda: Agenda = Agenda()

    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)
    agenda.armazenar_contato(contato3)

    agenda.imprimir_agenda()

    agenda.buscar_contato('rauy')

    agenda.imprimir_contato()

    agenda.remover_contato(contato3)

    agenda.imprimir_agenda()