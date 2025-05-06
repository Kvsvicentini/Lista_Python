while True:
    x = int(input("Digite um número menor que 5: "))
    
    if (x < 5):
        break
    else:
        print("Número inválido. Por favor, digite um número menor que 5. ")

print("Números pares entre", x, "e 20:")
for y in range(x, 21):
    if y % 2 == 0:
        print(y)