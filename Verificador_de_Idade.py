age = int(input("Digite sua idade: "))
if (age < 18):
    print(f"Você é menor de idade")
elif (age < 60):
    print(f"Você é maior de idade")
else:
    print(f"Você é uma pessoa idosa")