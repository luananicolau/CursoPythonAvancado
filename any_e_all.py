"""
Any e All

all() -> retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iteravel está vazio

any() -> retorna true se qualquer elemento do iteravel for verdadeiro. Se for vazio, false
"""

# exemplo all()

print(all([0, 1, 2, 3, 4])) # todos os números são verdadeiros? false
# Não! o 0 é False, portanto, o all retorna False

print(all([1, 2, 3, 4]))

print(all("Geek"))

nomes = ["Carlos", "Cristine", "Cassiano"]

# Se atente na diferença entre eles na saída do terminal.
print([nome[0] == "C" for nome in nomes])
print(all([nome[0] == "C" for nome in nomes]))

# Exemplo do any

print(any([num for num in [2, 3, 5, 7, 9] if num % 2 == 0]))