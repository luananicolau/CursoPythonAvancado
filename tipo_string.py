"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:41]) # Slice de String

print(nome[5:15]) # Slice de String


"""
#Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome= 'Angelina Jolie'
print(nome)
print(type(nome))

"""
[::-1] -> Comece do primeiro elemento, vá até o último e inverta 
"""

print(nome[::-1]) #Inversão da String Pythônico

print(nome.replace('e', 'i'))

print(type(nome))


