"""
Escrevendo em arquivos

#OBS: ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso já exista, o anterior será apagado e um novo será criado. Dessa forma, todo o conteudo no arquivo anterior
será perdido.

# exemplo de escrita - modo 'w' - write (escrita)

with open('novo.txt', 'w') as arquivo:
    arquivo.write('escrever dados em arquivo kekmdnkwn.\n')
    arquivo.write('quantas linhas quisermos.\n')
    arquivo.write('dd derfe dewad.\n')


"""


with open('geek.txt', 'w' )as arquivo:
    arquivo.write('luanalinda '* 1000)

