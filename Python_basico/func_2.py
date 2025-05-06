def num_pair(number):
    return number %2 == 0

#Exemplo de uso:
number = int(input("Digite um número para verificar se ele é par ou não: "))
if num_pair(number):
        print(f"O número digitado é par")
        
else:
        print(f"O número digitado é ímpar")