"""
Modos de abertura de arquivo

r -> abre para leitura - padrão
w -> abre para escrita - sobrescreve se o arquivo não existir
x -> abre para escrita somente se o arquivo não existir. caso o arquivo exista, FileExistsError
a -> abre para escrita, adicionando o conteudo ao final do arquivo. com o modo a, não controlamos o cursor
+ -> abre para o modo de atualização (leitura e escrita)

with open('university.txt', 'x') as arquivo:
    arquivo.write('testes de conteúdo. \n')
except FileExistsError:
    print('arquivo ja existe')
"""


