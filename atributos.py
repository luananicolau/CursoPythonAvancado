"""
POO - atributos

Atributos ->> representam as características do objeto. Ou seja, pelos atributos nós consgeuimos representar computacionalmente os estados de
um objeto

em python, dividimos os atributos em 3 grupos:
    - atributos de instância
    - atributos de classe
    - atributos dinâmicos

# atributos de instância: são atributos declarados dentro do método construtor

# OBS: método construtor : é um método especial utilizado para construção do objeto

# __init__ é o método construtor (cada classe tem a sua)

# Tudo que está dentro de uma classe é um método

# self - objeto executando o método

ps4 = Produto() - nada mais é que o __init__ sendo executado (método construtor)

# self não é necessario ser self mesmo, pode ser qualquer outra coisa, mas usualmente é 'self'

# se eu declarar um atributo como privado, so vou poder utilizar na propria classe, caso contrario, qualquer outra parte do projeto

# em python, por convenção, ficou establecido que todo atributo de uma classe é público. Caso queiramos que o atributo seja privado,
utiliza-se __ duplo underscore no início de seu nome.

isso é conhecido tbm como Name Mangling.



"""

# classes com atributos de instância públicos
class Lampada:
    def __init__(self,voltagem,cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome # o objeto usuario , no atributo nome, vai receber 'nome'
        self.email = email # o objeto usuario , no atributo email, vai receber 'email'
        self.senha = senha # o objeto usuario , no atributo senha, vai receber 'senha'

# Atributos Públicos e Atributos Privados

class Acesso:
    def __init__(self,email,senha):
        self.email = email
        self.__senha = senha

# Exemplo

user = Acesso('user@gmail.com', 123456)

print(user.email)

# print(user.__senha) # AttributeError
print(user._Acesso__senha) # temos acesso. Mas nao deveriamos fazer este acesso ( name mangling)


print(dir(user))

# oq significa atributos de instancia?

#significa que ao criarmos instancias/ objetos de uma classe, todas as instancia terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '534211')

# Atributos de classe - atributos declarados diretamente na classe, ou seja, fora do construtor

p1 = Produto('PlayStation 4', 'video game', 2300)
p2 = Produto('xbox s', 'video game', 4500)


# refatorar a classe Produto

class Produto:

    #Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

    p1 = Produto('PlayStation 4', 'video game', 2300)
    p2 = Produto('xbox s', 'video game', 4500)

print(p1.valor) #acesso possível, mas incorreto de um atributo de classe
print(p2.valor) #acesso possível, mas incorreto de um atributo de classe

# Obs: não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# Atributos Dinâmicos -> um atributo de instancia que pode ser criado em tempo de execução

# OBS: o atributo dinâmico será exclusivo da instância que o criou

p1 = Produto('playStation4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criand um atributo dinamico em tempo de execução

p2.peso = '5kg'

print(f'produto : {p2.nome}, Descrição: {p2.descricao}, valor : {p2.valor}, peso: {p2.peso}')

# Deletando Atributos

print(p1. __dict__)
print(p2.__dict__)

#print(Produto.__dict__)

del p2.peso
del p2.valor

print(p1.__dict__)
print(p2.__dict__)