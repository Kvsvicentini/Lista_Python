def check_prime_num(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

#Exemplo de uso:
num = int(input("Digite um número: "))
if check_prime_num(num):
    print("O número digitado é primo")
else:
    print("O número digitado não é primo")