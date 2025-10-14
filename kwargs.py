# Diferente do args que coloca os valores extra em uma tupla, o **kwargs EXIGE parâmetros nomeados
# O **kwargs transforma os argumentos em dicionários

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa.title()} é {cor}") # o ".title()" apenas faz
                                                             # a primeira letra ser maíuscula

cores_favoritas(marcos="verde", julia="azul", fernanda="azul", vanessa = "branco")

def mostrar_info(**kwargs):
    print("Dados recebidos:", kwargs)

    if "idade" in kwargs:
        print("Maior de idade" if kwargs["idade"] >= 18 else "Menor de idade")
    else:
        print("Idade não informada")

    if kwargs.get("cidade") == "São Paulo":
        print("Mora em São Paulo")
    elif "cidade" in kwargs:
        print(f"Mora em {kwargs['cidade']}")
    else:
        print("Cidade não informada")

    if "profissão" not in kwargs:
        print("Profissão não especificada")

mostrar_info(nome="João", idade=17, cidade="Campinas")

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Função com a ordem correta de parâmetros
def mostra_indo(a, b, *args, instrutor = "Geek", **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_indo(1, 2, 3, sobrenome="university", cargo="Instrutor"))