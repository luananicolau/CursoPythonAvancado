"""
Funções com Parâmetro Padrão (Default Parameters)

- funções onde a passagem de parãmetro seja opcional;

# Exemplo de função onde a passagem de parãmetros seja opcional
print('geek university')
print()

# Exemplo de função onde a passagem de parãmetros seja obrigatoria
def quadrado(numero):
    return numero **2

print(quadrado(3))]
print(quadrado()) #TypeError

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2,3))
print(exponencial(3,2))

print(exponencial(3))
print(exponencial(3,5))

# obs
# se o usuario passar somente 1 parâmetro, este será atribuido ao parâmetro número, e será calculado o quadrado deste número;
# se o usuario passar 2 argumentos, o primeiro sera atribuido ao parametro numero e o segundo ao parametro potencia. entao sera calculada esta potencia

print(exponencial())


# obs: em funçoes python, os parametros com valores default (padrao) devem sempre estar ao final da declaração

def mostra_informação(nome='geek', instrutor= False):
    if nome == 'geek' and instrutor:
        return 'bem-vindo instrutor geek'
    elif nome == 'geek':
        return 'eu pensei que voce era o instrutor'
    return f'ola{nome}'


print(mostra_informação())
print(mostra_informação(instrutor=True))
print(mostra_informação(True))
print(mostra_informação('ozzy'))
print(mostra_informação(nome='stephany'))

# exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,2,subtracao))

# escopo - evitar problemas e confusões

# variaveis globais
# variaveis locais

instrutor = 'geek' # variavel global

def diz_oi():
    instrutor = 'python' # variavel local
    return f'oi {instrutor}'

print(diz_oi())

#OBS: se tivermos uma variavel local com o mesmo nome de uma variavel global, a local terá preferencia

"""

