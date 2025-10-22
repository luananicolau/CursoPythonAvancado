"""
- métodos (funções) -> representam os comportamentos do objeto. Ou seja, as acoes que este objeto pode realizar no seu sistema[

Em Python, dividmos os métodos em 2 grupos : métodos de instancia e de classe

# métodos de instancia

# O metodo dunder init __init__ é um método especial chamado construtor e sua
função é construir o objeto a partir da classe.

OBS: todo elemento em python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS: os metodos/funcoes dunder em Python são chamados de métodos mágicos.

ATENÇÃO: por mais que possamos  criar nossas proprias funções utilizando dunder, não é aconselhado. Python possui vários métodos
com esta forma de nomenclatura ex:
def __correr__(self, metros):
print(f'{self.__nome} esta correndo {metros}metros')

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.__numero

    p1 = Produto('playsttaion 4 ', 'video game', 2300)

print(p1.desconto(10))

print(Produto.desconto(p1, 40)) # self, desconto

# Métodos de classe em Python são conhecidos como métodos estaticos em outras linguagens

"""



class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

        def desconto(self, porcentagem):
            """Retorna o valor do produto com o desconto"""
            return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'classe: {cls}')
        print(f'temos {cls.contador} usuario (s) no sistema')

    @classmethod
    def ver (cls):
        print('teste')

    @staticmethod
    def definicao():
        return 'UXR455'


    def __init__(self, nome,sobrenome,  email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.encrypt(senha, rounds=200000, salt_size= 16)
        Usuario.contador = self.__id
        print(f'usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123455')

print(user1.nome_completo())

nome = input('informe o nome: ')
sobrenome = input('informe o sobrenome: ')
email = input('informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome,email, senha)
else:
    print('usuario criado com sucesso!')


# Métodos de Classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

Usuario.conta_usuarios() # forma correta
user.conta_usuarios() # possivel, mas incorreta


def __gera_usuario(self):
    return self.__email.split('@')[0]

print(user._Usuario__gera_usuario()) # Acesso, de forma ruim...

#Método estático

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user.contador)

print(user.definicao())