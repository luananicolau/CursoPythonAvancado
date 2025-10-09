"""
funções com retorno


numeros = [1,2,3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

# OBS: em python, quando uma função não retorna nenhum valor, o retorno é none


# exemplo função

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()

print(f'retorno {ret}')

# vamos refatorar esta função para que ella retorne o valor

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()

print(f' retorno {ret}')

print(f'Retorno:{quadrado_de_7()} ')

# OBS: sobre a palavra reservada return

1- ela finaliza a função, ou seja, ela sai da execução da função;
2- podemos ter, em uma função, diferentes returns;
3- podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;


def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


def outra_funcao():
    return 2,3,4,5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))
"""
# Vamos criar uma função para jogar a moeda

from random import random

from ordered_dict import valor


def joga_moeda():
    # gera um numero pseudo-randomico entre 0 e 1
    if random > 0.5:
        return 'Cara'
    return 'coroa'

print(joga_moeda())

