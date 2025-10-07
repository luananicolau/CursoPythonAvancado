"""
Saindo de loops com break

Funciona na mesma forma que nas linguagens C ou Java

utilizamos o break para sair de loops de maneira forçada/ projetada
"""

# Exemplo 1

for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')

# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair:")
    if comando == 'sair':
        break
