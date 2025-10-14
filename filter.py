"""
filter

filter() - serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores)/ len(valores))

print(media)

# biblioteca para trabalhar com dados estatísticos

import statistics
# dados coletados em algum setor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'media : {media}')

res = filter(lambda valor: valor > media, dados)
print(list(res))

"""

# filter() serve para filtrad dados de coleção

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(media)

# Compare o resultado entre o map e o filter para ver a diferença
res = map(lambda x: x > media, dados)
print(list(res))

# filter() recebe como param, função e iterável tbm

# Se a condição for verdadeira ele retorna os dados
res = filter(lambda x: x > media, dados)
print(list(res))
print(list(res))  # Assim como no map, ele apaga após o uso.

# Mais exemplos

paises = ["", "Argentina", "", "Brasil", "Chile"]
print(paises)

res = filter(None, paises)
# res = filter(lambda pais: len(pais) > 0, paises) 2a forma
# res = filter(lambda pais: pais != "". paises) 3a forma
print(list(res))

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": ["Eu sou sigma", "oi betas"]},
    {"username": "laurinha", "tweets": []},
    {"username": "ken", "tweets": []},
]

print(usuarios)

# Filtrar os usuários que estão inátivos no twitter

inativos = list(filter(lambda usuario: len(usuario.get("tweets")) == 0, usuarios))

print(inativos)  # Dá todas as informações dos usuários
print([usuario.get("username") for usuario in inativos])  # Usando List Comprehension

# Combinando map() e filter()

nomes = ["Vanessa", "Ana", "Maria"]

lista = list(
    map(
        lambda nome: f"Sua instrutora é: {nome}",
        filter(lambda nome: len(nome) < 5, nomes),
    )
)

print(lista)