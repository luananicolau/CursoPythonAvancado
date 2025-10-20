"""
Higher Order Functions - HOP

O que isso significa??

- quando uma linguagem de programação suporte HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções como argumentos
para outras funções, e até mesmo criar variáveis do tipo de funções nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

# exemplo - definindo funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funçoes

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# nested functions - funções aninhadas

# em python podemos ter funções dentro de funções, que são conhecidas por nested functions ou inner functions (funções internas)

# exemplo

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('oi', 'suma daqui', 'chato'))
    return humor() + pessoa

print(cumprimento('luana'))

print(cumprimento('ana paula'))
"""
# retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('kkkk', 'hahaaha', 'auayyayayaa'))
    return rir()
rindo = faz_me_rir()
print(rindo)

