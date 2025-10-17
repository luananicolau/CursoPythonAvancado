"""
String IO

ATENÇÃO
Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - permissao de leitura
    - permissao de escrita

    StringIO -> utilizado para ler e criar arquivos em memória
"""

# promeiro fazemos o import
from io import StringIO

from leitura_de_arquivos import arquivo

mensagem ='string normal'

arquivo = StringIO(mensagem)

print(arquivo.read())

arquivo.write()

arquivo.seek(0)

print(arquivo.read())