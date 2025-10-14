"""
reduce

# imagine que vc tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# e vc tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y
    
- recebe a função e iteravel como map e filter

reduce(funcao, dados)

"""

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)