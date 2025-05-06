print("------------------------------------------------------------------------------------------------------------------------------")
print("Vamos ler dois números, compara-los, realizar operações matemáticas e mostrar o resultado se o resultado for par ou impar")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
if (num_1 < num_2):
    num_1 = num_1 + 10
    num_2 = num_2 / 2
else:
    num_1 = num_1 / 2
    num_2 = num_2 + 10
result = num_1 + num_2
comp = result % 2
if (comp == 0):
    print(f"O número é par")
else:
    print(f"O número é impar")