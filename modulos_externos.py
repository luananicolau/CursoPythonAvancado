"""
Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

https://pypi.org

colorama -> é utilizado para para permitir impressao de textos coloridos no terminal

pip install colorama

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'luana')

"""

from fpdf import FPDF

# Cria um objeto PDF
pdf = FPDF()

# Adiciona uma página
pdf.add_page()

# Define a fonte (nome, estilo, tamanho)
pdf.set_font("Arial", size=20)

# Adiciona texto
pdf.cell(200, 20, txt="Luana", ln=True, align='C')

# Salva o PDF
pdf.output("test_doc.pdf")
