"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em listas. o sort()
só funciona em listas

podemos utilizar o sorted() com qualquer iterável

como o próprio nome diz, sorted() serve para ordenar.

OBS : o sorted, SEMPRE retorna uma lista com os elementos do iterável ordenados

#Exemplo

numeros = [6, 1,8,2]
print(numeros)

print(sorted(numeros))
print(numeros)

"""
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros, reverse=True)) # ordena do maior para o menor

