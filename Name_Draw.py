
import random
names = []
print("Digite nomes para sortea-los.")
while True:
    name = input("Digite um nome:\n").strip()
    if name:
        names.append(name.strip())
    keep = input("Gostaria de continuar adicionando nomes? s/n:\n").lower()
    if (keep.lower() == 'n'):
        break
if names:
    raffle = random.choice(names)
    print(f"O nome sorteado foi: {raffle}")
else:
    print("Nenhum nome foi inserido para sortear")