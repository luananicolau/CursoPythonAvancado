"""
Definindo Funções

-Funções são pequenas partes do código que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos o curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;
"""
# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.append('roxo')

print(cores)

# Curso.append('mais dados...') #Attribute error
# Print(curso)

cores.clear()
print(cores)

# print(help(print))

# DRY - Don´t repeat yourself

# mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline;
parametros_de_entrada -> opcionais, onde tendo mais um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> também chamado de corpo da função ou implementação, é onde o processamento da função acontece. 
Neste bloco, pode ter ou não retorno da função

OBS: veja que para definir uma função, utilizamos a palavra 'def' informando ao python que estamos definindo uma
função. Também abrimos o bloco de código com o já conhecido dois pontos: que é utilizado em Python para definir blocos.

"""
# definindo a primeira função

def diz_oi():
    print('oi!')

"""
OBS:
1- veja que dentro das nossas funções podemos utilizar outras funções;
2- veja que nossa função só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi
3 - essa função não recebe nenhum parametro de entrada 
4- essa função não retorna nada 
"""

# utilizando funções

# chamada de execução
diz_oi()

"""
ATENÇAÕ:

nunca esqueça de utilizar o parênteses ao executar uma função.

exemplo: 

# Certo
diz_oi()
"""
def cantar_parabens():
    print('parabens pra voce')
    print('nesta data querida')

    cantar_parabens()

for n in range(5):
    cantar_parabens()

# Em python, podemos inclusive criar variáveis do tipo de uma função e executar esta função atraves da variavel

canta = cantar_parabens
canta()