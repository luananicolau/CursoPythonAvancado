"""
Módulo Random e o que são módulos?

- Em python, módulos são nada mais do que outros arquivos em python

módulo random -> possui varias funções para geração de números pseudo-aleatório.

#OBS: Existem duas formas de se utilizar um módulo ou função deste

# forma 1 - Imporatando todo o módulo (não recomendado)

import random
# random() -> gera um numero real pseudo-aleatorio entre 0 e 1

print(random.random())

# veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
# separados por ponto

# OBS: não confunda a função random() com pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo

from random import random

# do módulo random, importe a função random

for i in range(10):
    print(random())

# uniform() -> gera um  real pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3,7)) # 7 não é incluído


# randint() -> gera valores pseudo-aleatórios entre os valores estabelecidos

from random import randint

for i in range(6):
    print(randint(1,61), end= ',') # começa em 1 e vai até 60

# choice() -> mostra um valor aleatorio entre um iteravel

from random import choice
jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

# shuffle () -> tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2']

print(cartas)

shuffle(cartas)

print(cartas[0])
"""
