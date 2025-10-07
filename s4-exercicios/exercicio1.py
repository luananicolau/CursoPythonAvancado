numero1:int = int(input("Informe o primeiro número"))
numero2:int = int(input("Informe o segundo número"))

if numero1 > numero2:
    print(f"o numero {numero1} eh maior que {numero2}")
elif numero1 == numero2:

    print(f"os numeros {numero1} e {numero2} sao iguais.")
else:
    print(f"O numero {numero2} eh maior que {numero1}")