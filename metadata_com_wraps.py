"""
metadatas -< são dados intrísecos em arquivos.

wraps -> são funções que envolvem elementos com diversas finalidades

# problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        # eu sou uma funcao(logar) dentro de outra
        print(f' vc esta chamdno {funcao.__nome__}')
        print(f' aqui a documentaçaão: {funcao. __doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    #soma dois numeros
    return a + b

print(soma.__name__) # soma
print(soma.__doc__) # soma dois numeros

"""

# resolução do problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        # eu sou uma funcao(logar) dentro de outra
        print(f' vc esta chamdno {funcao.__nome__}')
        print(f' aqui a documentaçaão: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    #soma dois numeros
    return a + b

print(soma.__name__) # soma
print(soma.__doc__) # soma dois numeros