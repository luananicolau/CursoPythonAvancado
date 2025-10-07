contador: int = 0
indice: int = 1

while contador < 5:
    if indice % 3 == 0: # se o resto da divisão de indice por 3 for igual a 0, significa q eh multiplo de 3
        print(f'O numero {indice} eh multiplo de 3.')
        contador = contador + 1

    indice = indice + 1
