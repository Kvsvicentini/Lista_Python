print("--------------------------------------------------------------------------------------------------------")
print("Vamos ler dois números e mostra-los em ordem crescente")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
if (num_1 < num_2):
    print(f"A ordem dos números é {num_1}, {num_2}")
else:
    print(f"A ordem dos números é {num_2}, {num_1}")

#Outra maneira de realizar o exercício
'''
list = [num_1, num_2]
list.sort()
print(f"A ordem dos números é {list}")
'''