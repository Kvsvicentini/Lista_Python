print("--------------------------------------------------------------------------------------------------------")
print("Vamos ler dois números compara-los, somar cinco ao menor, compara-los novamente e mostrar o maior")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
if (num_1 < num_2):
    num_1 += 5
else:
    num_2 += 5
if (num_1 > num_2):
    print(f"O maior número é o {num_1}")
else:
    print(f"O maior número é o {num_2}")