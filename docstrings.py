"""
documentando funções com Docstrings

OBS : podemos ter acesso a documentação de uma função em python utilizando a propriedade especial __doc__

Podemos ainda fazer acesso á documentação com a função help()
"""

# exemplos

def diz_oi():
    """ uma função simples que retorna a string 'oi'"""
    return 'oi!'

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada
    :param numero:
    :param potencia:
    :return:
    """

    return numero ** potencia