"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos conjuntos da matemática

- aqui no python, os conjuntos são chamados de sets

dito isso, da mesma forma que na matemática :

-sets ( conjuntos) não possuem valores duplicados;
- sets (conjuntos) não possuem valores ordenados;
- eleementos não sao acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

os conjuntos (sets) são referenciados em python com chaves {}

Diferença entre conjuntos (set) e mapas (dicionarios) em python:
- um dicionario tem chave/ valor
- um conjunto tem apenas valor

# definindo um conjunto:

#Forma 1

s = set({1,2,3,4,5,5,6,7,2,3}) # repare que temos valores repetidos

print(s)
print(type(s))

# Obs:  ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e não fará parte do conjunto

# Forma 2 - mais comum

s = {1,2,3,4,5,5}
print(s)
print(type(s))


# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else :
    print('Tem o 3 ')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos

lista = [99, 2, 34, 23, 12, 1, 44, 5]
print(f'Lista: {lista}')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34,23, 12,1, 44,5)
print(f'Tupla: {tupla}')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99,2,34,23,2,12,1,44,5,34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto =  {99,2,34,23,2,12,1,44,5,34}
print(f'Conjunto: {conjunto} com {len(conjunto)}elementos')

# Assim como todo outro conjunto em Python podeos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s: print(valor)


# Usos interessantes com sets

# Imagina que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# Informam manualmente a cidade de onde vieram

#Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'São Paulo', 'Cuiaba']

print( cidades)
print(len(cidades))

print(len(set(cidades)))

# Adicionando elementos em um conjunto

s = {1, 2, 3}

s.add(4)
s.add(4) # duplicidade não gera erro, so é ignorado
print(s)

# Remover elementos em um conjunto
s = {1,2,3}
print(s)

#Forma 1

s.remove(3) # Não é indice!!!

print(s)

#Forma 2

s.discard(2)

print(s)


# Copiando um conjunto para outro...

# Forma 1 - deep copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

s = {1, 2, 3}
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)


s = {1, 2, 3}
print(s)


# Podemos remover todos os itens de um conjunto

s.clear()
print(s)


"""
