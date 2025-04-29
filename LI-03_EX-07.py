print("--------------------------------------------------------------------------------------------------------------------------------------")
print("Vamos ler três números e mostrar o resultado deles se o resultado for maior que 20")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))
calc_1 = num_1 + num_2 + num_3
if (calc_1 > 20):
    print(f"O resultado é maior que 20. O número é {calc_1}")