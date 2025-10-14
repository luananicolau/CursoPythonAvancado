"""
Zip

zip() -> cria um iterável (zip object) que agrega elemento de cada um dos iteráveis passados como entrada em pares


#Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# sempre podemos gerar uma lista, tupla ou dicionário


# o zip() utiliza como parametro o menor tamanho em iterável. isso significa que se estiver trabalhando com iteráveis
# de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar.

lista3 = [7, 8, 9,10, 11 ]

zip1 = zip(lista1, lista2,lista3)
print(list(zip1))
"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)