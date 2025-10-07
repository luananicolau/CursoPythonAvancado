"""
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1,2,3)

print(tupla[1])

Named tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parãmetros.

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

#Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

#Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca nome')

#Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

#Acessando dados

#forma 1

print(ray[0]) #idade
print(ray[1]) #raça
print(ray[2]) #nome

# forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))
"""

