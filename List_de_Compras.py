list = []
print("Vamos criar sua lista de compras, caso já tenha terminado, digite fim")
while True:
    item = input("Digite um item da lista de compras: ")
    if (item.lower() == 'fim'):
        break
    list.append(item)
print(f"Sua lista de compras: {list}")