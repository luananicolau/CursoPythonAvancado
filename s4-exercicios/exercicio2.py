numero: int = int(input("Informe um numero inteiro:"))

from math import sqrt
if numero > 0:
    print(f"A raiz quadrada de {numero} eh {sqrt(numero)}")
else:
    print(f"O numero {numero} eh invalido.")