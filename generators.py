from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof((x * 10 for x in range(1000)))

print("Para fazer a mesma tarefa gastamos em memória:")
print(f"List Comprehension: {list_comp} bytes")
print(f"Set Comprehension: {set_comp} bytes")
print(f"Dictionary Comprehension: {dic_comp} bytes")
print(f"Generator Expression: {gen} bytes")


gen = (x * 10 for x in range(1000))
print(gen)  # Aqui ele ainda não foi iterado, então fica vázio

for num in gen:  # Aqui está sendo iterado, então armazena mais memória
    print(num)