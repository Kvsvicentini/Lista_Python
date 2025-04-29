num = int(input("Digite um número e criaremos uma tabuada com o número digitado: "))
print(f"A tabuada do {num}:")
for i in range(1, 11,):
    print(f"{num} x {i} = {num * i}")