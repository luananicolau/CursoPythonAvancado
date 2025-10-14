listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3
"""
print(listas)
print(listas[0])
print(listas[0][1])
"""

# Iterando em lista aninhada com for
for lista in listas:
    for num in lista:
        print(num)

# Iterando em lista aninhada com List Comprehension
[[print(valor) for valor in lista] for lista in listas]


velha = [["X" if numero % 2 == 0 else "O" for numero in range(1, 4)] for numero in range(1, 4)]
print(velha)