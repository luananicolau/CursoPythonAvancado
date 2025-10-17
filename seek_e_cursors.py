"""
seek() -> é utilizada para movimentar o cursor pelo arquivo - recebe um parãmetro


from leitura_de_arquivos import arquivo

arquivo = open('texto.txt')

print(arquivo.read())

#movimetando o cursor pelo arquivo com a funçaõ seek() -> procurar
arquivo.seek(5)

print(arquivo.read())

from leitura_de_arquivos import arquivo

arquivo = open('texto.txt')

# readLine -> função que le o arquivo linha a linha

ret = arquivo.readline()

print(type(ret))

print(ret)

arquivo = open('texto.txt')

# readlines()

print(arquivo.readlines())

print(len(linhas))

# OBS: quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador
e o nosso programa. Essa conexão é chamada streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso
utilizamos a funçaão close().
"""
from leitura_de_arquivos import arquivo


arquivo = open('texto.txt')

print(arquivo.read())

print(arquivo.closed) # false verifica se o arquivo esta aberto ou fechado

arquivo.close()
