"""
Estruturas condicionais
if, else, elif

"""

idade = 23

"""
# Estrutura condicional if, em C 


if(idade < 18){
    printf("Menor de idade");
    }else if(idade == 18){
    printf("Tem 18 anos");
    }else{
    printf(É menor de idade");
    }
"""

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
