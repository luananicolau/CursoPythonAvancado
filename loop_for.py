"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < limitador; i++){
// execução do loop
}

Python

for item in interavel:
    // execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
    # Exemplo de for 1
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)


range(valor_inicial, valor_final)

OBS: O valor final não é incluido
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)

    Enumerate:

(0, 'G'), (1, 'E'), (2, 'E') , (3, 'K'), (4, ' ') ...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range (1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)


nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range (1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar?'))

for n in range(1, qtd+ 1) :
    print(f'Inprimindo [{n}')

for n in range(1, qtd+ 1) :
    num = int(input(f'Informe o {n}/{qtd}valor:'))
    soma = soma + num
print(f'A soma é {soma}')


"""

nome = 'Geek University'

for letra in nome:
    print(letra, end='') # end faz com que não pule uma linha a cada caractere

    





