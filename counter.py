"""
Módulo Collections - Counter

Collections -> High-performance Container Datetypes

Counter -> recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parãmetro e como valor a quantidade de
ocorrências desse elemento.

# Utilizando o Counter

from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1,1,1,2,2,3,3,3,3,1,1,2,2,4,4,4,5,5,5,5,3,45,45,66,66,43,34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

#Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências


# Exemplo 2

from collections import Counter

print(Counter('Geek University'))


"""

from collections import Counter

# Exemplo 3

texto = """Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa. Grosso modo, pode ser entendido como manifestação linguística das ideias de um autor, que serão interpretadas pelo leitor de acordo com seus conhecimentos linguísticos e culturais. Seu tamanho é variável."""

palavras = texto.split()

print(palavras)

res = Counter(palavras)

print(res)

#Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))