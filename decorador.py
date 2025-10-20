"""
# Decorar no sentido de aprimorar, não de memorizar

# Decorator Function - Função Decoradora


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um excelente dia!")

    return sendo_mesmo


@seja_educado_mesmo  # Decorator
def apresentacao():
    print("Meu nome é luana")


apresentacao()
"""