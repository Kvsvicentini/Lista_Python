# Loop para garantir que o número seja maior que 20
while True:
    x = int(input("Digite um número maior que 20: "))
    
    # Verifica se o número é maior que 20
    if (x > 20):
        break
    else:
        print("Número inválido. Por favor, digite um número maior que 20.")

# Exibe os números em ordem decrescente até 1
print("Números de", x, "a 1 em ordem decrescente:")
for y in range(x, 0, -1):
    print(y)