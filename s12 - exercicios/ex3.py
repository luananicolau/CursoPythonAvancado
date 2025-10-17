"""
3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este
arquivo possui.
"""

arquivo: str = input('Informe o nome do arquivo para abrir: ')

with open(arquivo, 'r') as arq:
    linhas = arq.readlines()

print(f'existe(m) {len(linhas)} linha(s) no arquivo.')