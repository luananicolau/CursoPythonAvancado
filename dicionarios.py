"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {},

print(type({}))


OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

    #  Criação de dicionários

# Forma 1 ( mais comum )

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

# Forma 2 - Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))


pais = paises.get('ru')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o pais')


# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('py','Não encontrado')
print(f'Encontrei o pais')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}print(f'Encontrei o pais')

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']



# Adicionar elementos em um dicionário

receita = {'jan':100, 'fev':120, 'mar':300}

print(receita)
print(type(receita))

# Forma 1

receita['abr']= 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário

# forma 1

receita['mai']= 550

print(receita)

# forma 2

receita.update({'mai': 600})

print(receita)

# Conslusão 1 : A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
# Conclusão 2 : em dicionários, NÃO podemos ter chaves repetidas.

# remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar':300}

print(receita)

#forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)

print(receita)

#OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado
#OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev']
print(receita)

# Se a chave não existir, será gerado um KeyError


# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário ( zerar dados)

d.clear()
print(d)

#Copiando um dicionário para outro

# Forma 1

novo = d.copy() # Deep Copy
print(novo)

novo['d'] = 4
print(d)
print(novo)

#forma 2 # Shallow Copy

novo = d

print(novo)

novo['d']= 4
print(d)

print(novo)

"""


# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# o método fromkeys recebe dois parâmetros: um iterável e um valor
# ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), 'novo')

print(veja)