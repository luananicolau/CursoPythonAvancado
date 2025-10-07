"""
Estruturas logicas : and (e), or (ou), not (não), is (é)

operadores unários:
    -not;

operadores binários:
    -and, or , is


Regras de funcionamento:

para o 'and', ambos os valores precisam ser True
para o 'or', um ou outro precisa ser True
para o 'not', o valor do booleano é invertido, ou seja, se for True, vira false, se for False vira True
para o 'is', o valor é comparado com um segundo. 
"""

ativo = True
logado = False

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Voce precisa ativar sua conta. Por favor, cheque seu e-mail')

