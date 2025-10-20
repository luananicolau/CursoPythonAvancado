"""
- geradores (generators) são iterators (iteradores):

OBS: o contrario não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- generators podem ser criados com funções geradoras;
- funções geradoras utilizam a palavra reservada yield;
- generators podem ser criados com Expressões Geradoras;

# Exemplo de Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: uma generator function não é um generator. Ela gera um generator!!!!

gen = conta_ate(5)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

