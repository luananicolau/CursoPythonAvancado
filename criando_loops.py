"""
Criando sua própria versão de loop

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'luana gata':
    print(letra)
"""

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('luana gata')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)

