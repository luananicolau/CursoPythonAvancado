"""
PDB -> Python Debugger

Vida de Inseto -> Life's Bug

o debug é basicamente pra gente ver "por trás" do código e facilitar o entendimento do que possivelmente esta dando errado

"""
# É possível debugar com print, mas não é boa prática

"""
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f"Ocorreu um problema {err}")


print(dividir(4, 7))

"""


# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = "Angelina"
sobrenome = "Jolie"


breakpoint()  # pdb.set_trace();import pdb  # O import vem aqui, pq provavelmente só usar aqui
nome_completo = nome + " " + sobrenome
curso = "Programção em Python: Essencial"
final = nome_completo + " faz o curso " + curso
print(final)
