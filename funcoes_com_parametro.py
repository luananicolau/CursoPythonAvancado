"""
funçoes com parametro (de entrada)

- funções que recebem dados para serem processados dentro da mesma:

se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- não possuem entrada;
- não possuem saída;
- possuem entrada mas não possuem saida;
- nao posssuem entrada mas possuem saida;
- possuem entrada e saida;


# Refatorando uma função

def quadrado(numero):
#    return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado()) # TypeError


# refatorando a funçao


def cantar_parabens(aniversariante):
    print('parabens pra voce')
    print('nesta data querida')
    print(f'viva o {aniversariante}')

cantar_parabens('Patricia')


def soma(a,b):
    return a + b

def multiplica(num1, num2):
    return num1*num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2,5))
print(soma(10,20))

print(multiplica(4,5))
print(multiplica(2,8))

print(outra(3,2, 'geek'))
print(outra(5,4, 'python'))

# obs: se a gente informar um numero errado de parâmetro ou argumento, teremos TypeError
"""

# nomeando parãmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# A diferença entre parâmetros e argumentos

# parametros sao variaveis decladradas na definição de uma função;
# argumentos são dados passados durante a execução de uma função;

# A ordem dos parãmetros importa!

nome = 'felicity'
sobrenome = 'jones'

print(nome_completo(sobrenome, nome))
# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.

