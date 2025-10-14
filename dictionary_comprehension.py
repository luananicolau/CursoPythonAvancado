numeros = {'a': 1, 'b': 2, 'c': 3}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

lista_numeros = [1, 2, 3 , 4, 5, 6]

res = {num: ("par" if num % 2 == 0 else "impar") for num in lista_numeros}

print(res)
print(type(res))