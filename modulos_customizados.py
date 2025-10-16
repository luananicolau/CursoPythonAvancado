"""
Como módulos Python nada mais são que arquivos python, então todos os arquivos que criamos neste curso
são módulos python prontos para serem utilizados

# importando uma função especifica do nosso modulo


from funcoes_com_parametro import soma_impares

print(soma_impares([1,2,3,4,5,6,7,8,9]))

# importando todo o módulo ( temos acesso a TOODS  os elementos do módulo
import funcoes_com_parametro as fcp

# estamos acessando e imprimindo uma variavel contida no módulo
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""
