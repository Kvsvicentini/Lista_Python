print("--------------------------------------------------------------------------------------------------------")
print("Vamos ler três números e compara-los entre eles e somar cinco ao menor valor e mostrar o resultado")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))
if (num_1 < num_2):
    if ( num_3 < num_1):
        result_1 = num_3 + 5
        print(f"{num_3} + 5 = {result_1}")
    else:
        result_1 = num_1 + 5
        print(f"{num_1} + 5 = {result_1}")
else:
    if (num_2 < num_3):
        result_1 = num_2 + 5
        print(f"{num_2} + 5 = {result_1}")
    else:
        result_1 = num_3 + 5
        print(f"{num_3} + 5 = {result_1}")
        
#Outra maneira de fazer o exercício
'''
list = [num_1, num_2, num_3]
result_1 = min(list) + 5
print(f"O resultado da conta de {min(list)} + 5 = {result_1}")
'''