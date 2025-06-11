import random
num_secret = random.randint(1, 10)
cont = 0
print("Tente adivinhar o número sorteado de 1 a 10")
while True:
    attempt = int(input("Digite um número: "))
    cont += 1
    if attempt == num_secret:
        print(f"Parabéns! Você acertou o número depois de {cont} vezes, o número era {num_secret}")
        break
    else:
        print(f"Errou! Tente novamente.")