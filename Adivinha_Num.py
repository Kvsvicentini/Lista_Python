import random
num_secret = random.randint(1, 10)
attempt = int(input("Tente adivinhar o número sorteado de 1 a 10: "))
if attempt == num_secret:
    print(f"Parabéns! Você acertou o número, o número era {num_secret}")
else:
    print(f"Errou! O número era {num_secret}.")