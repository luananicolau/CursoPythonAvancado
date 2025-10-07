"""
Modulo Collections - deque

Podemos dizer que o deque é uma lista de alta performance
"""

#importa

from collections import deque

# criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona no final

print(deq)

deq.appendleft('k') # adiciona no começo

print(deq)

# Remover elementos

print(deq.pop()) # remove e retorna o ultimo elemento

print(deq)

print(deq.popleft()) # remove e retorna o primeiro elemento

print(deq)
