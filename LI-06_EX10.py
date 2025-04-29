# Loop para garantir que o número esteja entre 5 e 10
while True:
    x = int(input("Digite um número entre 5 e 10: "))
    
    # Verifica se o número está dentro do intervalo
    if (5 <= x <= 10):
        break
    else:
        print("Número inválido. Por favor, digite um número entre 5 e 10.")

# Exibe o número digitado
print("O número digitado foi:", x)