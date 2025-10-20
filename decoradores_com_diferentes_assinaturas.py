"""
Decorators com diferentes assinaturas

# para resolver, utilizamos um padrão de projeto chamado Decorator Pattern



# relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'ola eu sou {nome}'
@gritar
def ordenar(principal, acompanhamento):
    return f'ola eu gostaria de {principal}, acpmapanhado de {acompanhamento}'

print(ordenar('picanha', 'batata frita'))

# Com Decorator Patter

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs ). upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'ola eu sou {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'ola, eu gostaria de {principal}acompanhado de {acompanhamento}'

print(saudacao('felicity'))

print(ordenar('picanha', 'batata frita'))

@gritar
def lol():
    return 'lol'

print(lol())

# podemos utilizar parametros nomeados

print(ordenar(acompanhamento='batata frita', principal='picanha'))

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'valor incorreto! primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

print(soma_dez(10, 12))
print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))

print(comida_favorita('sanduiche', 'pizza'))
"""




