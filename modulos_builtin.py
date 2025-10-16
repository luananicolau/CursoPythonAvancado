"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random)


# Podemos importar todas as funções deum módulo utiliando o *

from random import *
# import random

print(random())

# importando todo o módulo

import random

print(random.random())

# utilizando alias (apelidos) para modulos/ funcoes

from random import randint as rdi, random as rdm

print(rdi(5,89))

print(rdm())

# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo modulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

"""

