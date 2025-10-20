"""
Iterator ->
- um objeto que pode ter iterado.
- um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada:

iterable ->
- um objeto que irá retornar um iterator quando a função iter() for chamada.

nome = 'luana' #é um iterable, mas nao é um iterator
numeros = [1, 2, 3, 4, 5, 6] # é um iterable mas não é um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

"""
nome = 'drake'

for letra in nome:
    print(f'{letra}')

