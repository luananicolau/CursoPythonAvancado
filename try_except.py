"""
Utilizamos o try/except para tratar error que podem ocorrer no nosso código. Previnindo assim que o programa pare de funcionar
e o usuario receba mensagens de erro inesperadas

forma geral:

try:
    // execução problematica
except:
    // o que deve ser feito em caso de problema


# Exemplo 1

try:
    geek()
except:
    print('deu erro')

# tente executar a função geek(), caso voce encontre erros, imprima a mensagem de erro

# Tratando um erro específico

try:
    geek()
except NameError:
    print('vc esta utilizando uma função inexistente')


# Tratando um erro específico com detalhes do erro

try:
    len(5)
except NameError as err:
    print(f'a aplicação gerou o seguinte erro: {err}')
"""


