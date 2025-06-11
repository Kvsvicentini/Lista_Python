num = int(input("Digite um número e criaremos uma tabuada com o número digitado: "))
operation = input("Digite a operação que deseja utilizar na tabuada: +, -, *, / \n")
if (operation == "*"):
    print(f"A tabuada do {num}:")
    for i in range(1, 11,):
        print(f"{num} x {i} = {num * i}")
elif (operation == "+"):
    print(f"A tabuada do {num}:")
    for i in range(1, 11,):
        print(f"{num} + {i} = {num + i}")
elif (operation == "-"):
    print(f"A tabuada do {num}:")
    for i in range(1, 11,):
        print(f"{num} - {i} = {num - i}")