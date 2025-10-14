"""
set comprehension

lista = [1,2,3,4,5]
set = {1,2,3,4,5}
"""


numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x ** 2 for x in range(1, 11)}
print(numeros)

numeros = {x: x ** 2 for x in range(1, 11)} # Facilmente vira um Dict Comprehension
print(numeros)

letras = {letra for letra in "luana nicolau"} # Não se repete e não fica em ordem
print(letras)