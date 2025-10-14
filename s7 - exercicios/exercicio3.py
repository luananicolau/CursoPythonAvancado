# Enunciado 1
print("1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.")


def dobrar(numero: int):
    """Recebe um número inteiro e retorna o seu dobro."""
    return numero * 2


print(f"O dobro do valor é {dobrar(5)}.")

# Enunciado 2
print("2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e")
print("   imprima ela por extenso como “1 de janeiro de 2024”.")


def data_por_extenso(data: str) -> str:
    """Recebe uma data no formato 'dd/mm/aaaa' e retorna por extenso."""
    meses = {
        "01": "janeiro", "02": "fevereiro", "03": "março", "04": "abril",
        "05": "maio", "06": "junho", "07": "julho", "08": "agosto",
        "09": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"
    }

    dia, mes, ano = data.split("/")
    dia = str(int(dia))  # remove zero à esquerda
    mes_extenso = meses.get(mes, "mês inválido")
    return f"{dia} de {mes_extenso} de {ano}"


# Exemplo de uso:
entrada = input("Digite a data no formato dd/mm/aaaa: ")
print("Data por extenso:", data_por_extenso(entrada))

# Enunciado 3
print("3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.")


def maior_valor(lista=[]):
    print(max(lista))


maior_valor([1, 2, 3, 4])