print("Vamos ler um número e mostrar o seu valor")
while True:
    x = float(input("Digite um número: "))
    if ( x >= 10):
        print(f"O número digitado é: {x}")
        break
    else:
        print("Número inválido, tente novamente")