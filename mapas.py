"""
Mapas -> conhecidos em Python como dicionários

Dicionarios em pythoon são representados por chaves {}

# Interar sobre dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave}: {receita[chave]}')


# Acessando as chaves
print(receita.keys())

for chave in receita.keys():

    print(receita[chave])


# acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)


receita = {'jan':100, 'fev':250, 'mar':400}

print(receita)

# desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave= {chave} e valor ={valor}')

    # Soma*, Valor Maximo*, valor Minimo*, Tamanho

# * Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""

