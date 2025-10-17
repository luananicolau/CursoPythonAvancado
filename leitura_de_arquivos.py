"""
Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> na forma mais simples de utilização nós passamos por apenas um parâmetro de ntrada,que nesse caso é o
nome do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

mode r -> Modo de leitura. r-> read() -> ler
"""

#Exemplo
arquivo = open('texto.txt')

#print(arquivo)

#print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
#print(arquivo.read())