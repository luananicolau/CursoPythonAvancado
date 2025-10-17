"""
o bloco with

#1 - abrimos o arquivo
#2 - manipulamos o arquivo
#3- fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.


# forma pythônica de manipular arquivos
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed())

print(arquivo.read())
"""

