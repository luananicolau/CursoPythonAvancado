"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula
"""

ativo = False
print(ativo)

"""
Operações básicas:
"""

# Negação (not):

"""
fazendo a negação, se o valor booleano for verdadeiro o resultado será falso.
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.

"""
print(not ativo)

logado = True

# Ou (or):

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or true -> true
True or false -> true
False or true -> true
False or false -> false

"""

print(ativo or logado)