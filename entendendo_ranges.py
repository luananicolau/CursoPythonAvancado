"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo de 1 em 1 )

for num in range ( 4, 11) :
    print(num)


    # Forma 3

range(valor_de_inicio, valor_de_parada, passo)

# Exemplo forma 3
for num in range(1, 10, 2):
    print(num)


#Forma 4 (Inversa)

for num in range (10, -1, -1):
    print(num)

"""



