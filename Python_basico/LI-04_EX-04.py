print("--------------------------------------------------------------------------------------------------------")
print("Vamos ler três números e compara-los para mostrar o maior")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: ")) 
if (num_1 > num_2):
    if (num_1 > num_3):
        print(f"O maior número é {num_1}")
    else:
        print(f"O maior número é {num_3}") 
else:
    if (num_2 > num_3):
        print(f"O maior número é {num_2}")
    else:
        print(f"O maior número é {num_3}")
#Outra maneira de fazer o exercício
#list = {num_1, num_2, num_3}
#print(f"O maior número é {max(list)}")