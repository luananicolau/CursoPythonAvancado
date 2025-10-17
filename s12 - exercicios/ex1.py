"""
 1. Crie um programa que.
 a) Crie/abra um arquivo texto de nome “arq.txt”
 b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere
“0”.
 c) Feche o arquivo
 d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.
"""

with open('arq.txt', 'a') as arquivo:
    while True:
        caractere: str = input('Informe um caractere ou 0 para sair: ')

        if caractere != '0':
            arquivo.write(f'{caractere}\n')
        else:
            break

with open('arq.txt', 'a') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha)