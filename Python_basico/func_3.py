def factorial(num_1):
    num_2 = 1
    for i in range(1, num_1 + 1):
        num_2 *= i
    return num_2

#Exemplo de uso:
num_1 = int(input("Digite um número para mostrarmos seu fatorial: "))
print(f"O resultado de {num_1}! = {factorial(num_1)}")