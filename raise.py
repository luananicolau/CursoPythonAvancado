"""
levantando os próprios erros com raise

raise -> lança exceções

OBS: o raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra

para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens
de erro

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')


# Exemplo real

def colore(texto,cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto}será impresso na cor {cor}')

    colore('True',7)
"""

