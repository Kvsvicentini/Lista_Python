print("Vamos ler dois números, compara-los com 5 e 10 e mostrar os números lidos" )
while True:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um segundo número: "))
    if (num1 < 5 and num2 > 10):
        print(f"Os números digitados são: {num1} e {num2}")
        break
    else:
        print("Números inválidos. Tente novamente")
