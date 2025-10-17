"""

import os
import tempfile

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists("seek_e_cursors.py"))
print(os.path.exists("novo.txt"))
print(os.path.exists("luana.py"))

# Diretório

print(os.path.exists("C:\\Users"))
print(os.path.exists("estudando-python"))

# Criando arquivos
# os.mknod("arquivo-criado.txt") - no windows vai dar erro, apenas linux!!!

# Para criar multiplataforma
with open("arquivo_criado.txt", 'w'):
    pass


os.makedirs("teste1_criando_dir", exist_ok=True) # Esse funciona!

# Renomear arquivos e diretórios

if os.path.exists("luana.txt"):
    os.rename("luana.txt", "vini.txt")

# Se existe o diretório, renomeie
if os.path.exists("C:\\Users\\vlenc\\OneDrive\\Documentos\\estudando-python\\estudando-python\\secao12-leitura-escrita-arquivos\\teste_criando_dir"):
    os.rename(
        "C:\\Users\\luana\\OneDrive\\Documentos\\estudando-python\\estudando-python\\secao12-leitura-escrita-arquivos\\teste_criando_dir",
        "C:\\Users\\luana\\OneDrive\\Documentos\\estudando-python\\estudando-python\\secao12-leitura-escrita-arquivos\\novo_criando_dir"
    )
else:
    print("O diretório não existe")

os.rmdir("teste1_criando_dir") # Remover dir vazio


# Diretório temporário:
with tempfile.TemporaryDirectory() as tmp:
    print(f"Criei o diretório temporário e, {tmp}")
    with open(os.path.join(tmp, "arquivo_temporario.txt"), "w") as arquivo:
        arquivo.write("arquivo temp\n")
    input() # Quando sai do "with" o arquivo é apagado, então deixa essa input só pra "ganhar tempo"


 Arquivo temporário - Não funciona no windows
with tempfile.TemporaryFile as tmp:
    tmp.write(b"Vini Lenci\n")
    tmp.seek(0)
    print(tmp.read())


"""