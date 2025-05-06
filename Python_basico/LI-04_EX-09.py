print("-----------------------------------------------------------------------------------------------------------------------------------------")
print("Vamos ler quatro números, realizar operações matemáticas e mostrar o número com as mensagens de se for menor que 10 ou maior que 10")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))
num_4 = float(input("Digite o quarto número: "))
calc_1 = num_1 + num_2
calc_2 = num_3 - num_4
result = calc_1 + calc_2
if (result > 10):
    print(f"Número maior que 10. O resultado das operações deu {result}")
else:
    print(f"Número menor que 10. O resultado das operações deu {result}")