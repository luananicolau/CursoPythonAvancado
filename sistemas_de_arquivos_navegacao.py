"""
Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operating System

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretorio de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

import os


# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('home/geek/')) #True

# Windows

print(os.path.isabs('C:\\Users\\geek'))

# podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (linus e Mac) nt (windows)

import sys
print(sys.platform)

import os

# podemos listar os arquivos e diretórios com o listdir()

print(os.listdir('/etc'))

Para mais detalhes - scandir()




print(os.getcwd()) # Caminho absoluto do arquivo atual

res = os.path.join(os.getcwd(), "teste_SO")

# os.chdir(res) -> vai dar erro pq não existe esse diretório

# print(os.getcwd())
"""
