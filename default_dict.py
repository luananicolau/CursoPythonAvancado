"""
Módulo Collections - Default Dict

# recap dicionarios

dicionario = {'curso': 'Programação em Python: Essencial '}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) #??? Keyerror

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentamos acessar uma chave que não existe, essa chave será criada e o valor default será atribuido

# OBS: lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e receber valores

"""
# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não

print(dicionario)