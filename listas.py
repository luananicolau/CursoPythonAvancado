"""
Listas

Listas em python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem dinâmicos e também de podemos colocar QUALQUER tipo de dado.

Linguagens C/ Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmico: Não possui tamanho fixo. Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;

As listas em Python são representadas por colchetes: []


# Podemos facilmente checar se determinado valor está contido na lista

if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8 ')


num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')


# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56) #Erro

lista1.append([8, 3, 1]) # coloca a lista como elemento unico (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) #coloca cada elemento da lista como valor adicional á lista
print(lista1)

#podemos inserir um novo elemento na lista informando a posição do índice
#OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

#Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

lista1.extended(lista2)
print(lista1)

type ([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e',' r','s','i','t','y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')


#Podemos facilmente inverter uma lista
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

#Forma 2
print(lista1[::-1]) #significa que começa na posição 0, vai até o final e inverte
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

#quantidade de elementos em uma lista
print(len(lista1))

# Podemos remover facilmente o ultimo elemento de uma lista
# OBS: o pop não somente remove o ultimo elemento mas tambem retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS:  os elementos á direita desse índice serão deslocados para a esquerda
# OBS: Se não houver elemento no índice informado, teremos o erro Indexerror.
lista5.pop(2)
print(lista5)


# podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)

# OBS:  por padrão, o split separa os elementos da lista pelo espaço entre elas.

# exemplo 2
curso = 'Programação em python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['programação', 'em', 'python:', 'essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string

curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: pega a lista 6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 454545454]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - utilizando for

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)


# Exemplo 2 - utilizando while

carrinho = [ ]
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
     carrinho.append(produto)

for produto in carrinho:
    print(produto)

#Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# fazer acesso aos elementos de forma indexada inversa
print(cores)[-1]) #branco
print(cores)[-2]) #azul
print(cores)[-3]) #amarelo
print(cores)[-4]) #verde
print(cores)[-5]) #erro, pois não existe indice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice +1

# gerar indice em um for
    for indice, cor in enumerate(cores):
        print(indice, cor )


#listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(42)

print(lista)

# encontrar o indice de um elemento em uma lista

numeros = [ 5,6,7,5,8,9,10]

# em qual indice da lista está o valor 6? / 9?
print(numeros.index(6))
print(numeros.index(9))

#OBS: caso não tenha esse elemento na lista, será apresentado erro ValueError

#Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5,1))# buscando a partir do indice 1
print(numeros.index(5,2))# buscando a partir do indice 2
print(numeros.index(5,3))# buscando a partir do indice 3

#OBS: caso não tenha esse elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))# Buscar o indice do valor 8, entre os indices 3 a 6


# Revisão de slicing

# lista[inicio:fim:passo]
#range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) #Iniciando no índice 1 e pegando todos os relementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista[:2]) # começa em 0, pega até o indice 2 - 1

print(lista[:4]) # começa em 0, pega até o indice 4 - 1

print(lista[1:3]) # começa em 1, pega até o indice 3 - 1

# Trabalhando com slice de lista com parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2

print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes.reverse()
print(nomes)


# Soma*, Valor Máximo*, Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) #soma
print(max(lista)) #maximo valor
print(min(lista)) #minimo valor
print(len(lista)) #tamanho da lista

# transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

#OBS: Se tivermos mais elementos para desempacotar do que variáveis para receber os dados, teremos Valueerror


# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

# veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. isso em Python
# é chamado Deep Copy (cópia profunda)


# Forma 2

lista = [1, 2, 3]
print(lista)

nova = lista # Cópia
print(nova)

nova.append(4)

print(lista)
print(nova)

# veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy
"""

