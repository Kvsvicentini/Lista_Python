print("--------------------------------------------------------------------------------------------------------")
print("Vamos ler três números e mostra-los em ordem crescente")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))
if (num_1 < num_2):
    if (num_1 < num_3):
        if (num_3 < num_2):
            print(f"A ordem dos números é {num_1}, {num_3}, {num_2}")
        else:
            print(f"A ordem dos números é {num_1}, {num_2}, {num_3}")
    else:
        print(f"A ordem dos números é {num_3}, {num_1}, {num_2}")
else:
    if (num_2 < num_3):
        if (num_3 < num_1):
            print(f"A ordem dos números é {num_2}, {num_1}, {num_3}")
        else:
            print(f"A ordem dos números é {num_2}, {num_1}, {num_3}")
    else:
        print(f"A ordem dos números é {num_3}, {num_2}, {num_1}")
        
#Outra maneira de realizar o exercício
'''
list = [num_1, num_2, num_3]
list.sort()
print(f"A orde dos números é {list}")
'''