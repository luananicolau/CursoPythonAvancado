"""
Lambdas são funções sem nome, ou seja, funções anônimas


lambda x: 3 * x + 1

# e como utilizar a expressão lambda?
calc = lambda x: 3 * x+1

print(calc(4))
print(calc(7))
"""


lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1

print(calc(4))

nome_completo = (
    lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
)

print(nome_completo("luana", "nicolau"))

cantores = [
    "Felipe Tito",
    "Matheus Brasileiro",
    "Yunk Vino",
    "Playboi Carti",
    "Thiago Veigh",
    "Ryu, The Runner",
]
print(cantores)

cantores.sort(
    key=lambda sobrenome: sobrenome.split(" ")[-1].lower()
)  # O "[-1]" serve para falar que quer a segunda parte da string
print(cantores)


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + 2 * b + c"""
    return lambda x: a * x**2 + 2 * b + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(1))

print(geradora_funcao_quadratica(3, 0, 1)(2))