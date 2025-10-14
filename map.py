"""
Map

Com map, fazemos mapeamento de valores para função.

"""

import math

def area(r):
    """Calcule a área de um circulo com raio 'r'"""
    return math.pi * (r**2)

print(area(2))
print(area(5.3))

raios = [2,5,7.1,0.3,10,44]

# forma comum
areas = []
for r in raios:
    areas.append((area(r)))
    print(areas)

# forma 2 - map

# map é uma função que recebe dois parâmetros: o primeiro a função, o segundo um iterável. Retorna um Map Object

areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

# forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

#OBS: após utilizar a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função

# O map Object: f(a1), f(a2), f(...), f(an)

