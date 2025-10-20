"""
Decorators

- decoradores são funções;
- decoradores envolvem outras funções e aprimoram seus comportamentos;
- decoradores também são exmeplos de Higher Order Functions;
- decorators tem uma sintaxe própria, usando "@" ( Syntact Sugar / açúcar sintético)


# decorators como funções (sintaxe não recomendada / sem açúcar sintático)

def seja_educado(funcao):
    def sendo():
        print('foi um prazer conhecer vc')
        funcao()
        print('tenha um otimo dia')
        return sendo()

def saudacao():
    print('seja bem vindo')

# testando 1

# saudacao()

teste = seja_educado(saudacao)
teste()

# teste 2
def raiva():
    print('te odeio')

raiva_educada = seja_educado(raiva)
raiva_educada()


# decorators com Syntax Sugar ( açúcar sintético)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('foi um prazer conhecer vc')
        funcao()
        print('tenha um excelente dia')
        return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('meu nome é Luana')

    apresentando()

def dormir():
    print('quero dormir...')

    dormir()

# OBS: não confunda decorator com decorator function
"""

