num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação matemática (+, -, *, /): ")
if (operacao == '+'):
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
elif (operacao == '-'):
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
elif (operacao == '*'):
    print(f"{num_1} * {num_2} = {num_1 * num_2}")
elif (operacao == '/'):
    print(f"{num_1} / {num_2} = {num_1 / num_2}")
else:
    print("Operação inválida.")