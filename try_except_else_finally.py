"""
Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: a função do usuario é destruir seu sistema

num = int(input('Informe um número: '))
print(f'Voce digitou {num}')

# else -> é executado somente se nao ocorrer o erro

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('valor incorreto')
else:
    print(f'vc digitou {num}')


# Finally - utilizao geralmente para fechar ou desalocar recursos

try:
    num = int(input('informe um numero: '))
except ValueError:
    print('vc nao digitou um valor valido')
else:
    print(f'vc digitou o numero {num}')
finally:
    print('executando o finally')

"""


