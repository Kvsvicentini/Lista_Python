print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Vamos ler um número, ver se ele é maior que dez, somar cinco se for maior e se for menor ou igual a 10, somaremos 20 e mostrar o resultado se for maior que 25")
num_1 = float(input("Digite um número: "))
if (num_1 <= 10):
    num_1 += 5
else:
    num_1 += 20
if (num_1 > 25):
    print(f"O resultado é {num_1}")