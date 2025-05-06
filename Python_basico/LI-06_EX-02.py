print("---------------------------------------------------------------------------------------------------------------------------")
# Solicita ao usuário que insira um número
x = int(input("Digite um número: "))

# Verifica se o número é menor que 20
if (x < 20):
    # Exibe os números de 'numero' até 20
    for y in range(x, 21):
        print(y)
else:
    print("O número digitado é maior ou igual a 20.")