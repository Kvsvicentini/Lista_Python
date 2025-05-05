def add_shopping_list(shopping):
    buy = input("Digite um produto para a lista de compras: ")
    shopping.append(buy)
    print("Produto adicionado")

def list_shopping_list(shopping):
    if shopping:
        print("\nProdutos na lista de compras:")
        for i, buy in enumerate(shopping, 1):
            print(f"{i}. {buy}")
    else:
        print("A lista de compras está vazia")

def remove_shopping_list(shopping):
    if not shopping:
        print("Não há produtos na lista de compras para remover")
        return
    list_shopping_list(shopping)
    try:
        num = int(input("Digite o número do produto a ser excluído: "))
        if 1 <= num <= len(shopping):
            remove_buy = shopping.pop(num - 1)
            print(f"Produto: '{remove_buy}' removido com sucesso.")
        else:
            print("Número do produto inválido")
    except ValueError:
        print("Digite um número válido.")

def menu():
    print("\nEscolha uma opção")
    print("1-Adicionar um produto a lista de compras")
    print("2-Listar os produtos da lista de compras")
    print("3-Remover um produto da lista de compras")
    print("4-Sair do sistema")

def main():
    shopping = []
    print("\nVamos criar uma lista de compras.")

    while True:
        menu()

        try: 
            option = int(input("\nDigite a opção que deseja: "))
        except ValueError:
            print("Digite um número válido.")
            continue
        match option:
            case 1:
                add_shopping_list(shopping)
            case 2:
                list_shopping_list(shopping)
            case 3:
                remove_shopping_list(shopping)
            case 4:
                print("Saindo do sistema.")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

'''''
list = []
print("Vamos criar sua lista de compras, caso já tenha terminado, digite fim")
while True:
    item = input("Digite um item da lista de compras: ")
    if (item.lower() == 'fim'):
        break
    list.append(item)
print(f"Sua lista de compras: {list}")
'''''