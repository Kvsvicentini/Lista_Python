users = []
while True:
    name = input("Digite seu nome: ")
    age = int(input("Digite sua idade: "))
    users.append({"Nome": name, "Idade": age})
    keep = input("Deseja cadastrar outro? (s/n): ").lower
    if (keep != 's'):
        break
print("\nUsuários cadastrados:")
for i in users:
    print(f"{i['Nome']} - {i['Idade']} anos")