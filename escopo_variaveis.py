"""
Escopo de Variáveis

/                      /

Dois casos de escopo:

1- Variáveis globais;
    -variáveis globais são reconhecidas, ou seja, seu esocpo compreende todo programa.

2- Variáveis locais;
    -variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarado.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagemm de tipagem dinâmica. Isso significa que ao declararmos uma variável,  nós não colocamos o
tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor a mesma.

Exemplo em C:
int numero =42;

Exemplo em Java:
int numero = 42;

"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10 # A variável "novo" está declarada localmente dentro do bloco do if. Portanto, é local.
    print(novo)

    print(novo)