def add_tasks(tasks):
    task = input("Digite uma tarefa: ")
    tasks.append(task)
    print("Tarefa adicionada")

def list_tasks(tasks):
    if tasks:
        print("\nTarefas cadastradas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("A lista está vazia")

def remove_tasks(tasks):
    if not tasks:
        print("Não há tarefas para remover")
        return
    list_tasks(tasks)
    try:
        num = int(input("Digite o número da tarefa a ser excluído: "))
        if 1 <= num <= len(tasks):
            remove_task = tasks.pop(num - 1)
            print(f"Tarefa {remove_task} removida com sucesso.")
        else:
            print("Número da tarefa inválido")
    except ValueError:
        print("Digite um número válido.")

def menu():
    print("\nEscolha uma opção")
    print("1-Adicionar uma tarefa")
    print("2-Listar as tarefas")
    print("3-Remover uma tarefa")
    print("4-Sair do sistema")

def main():
    tasks = []
    print("\nVamos criar uma lista de tarefas.")

    while True:
        menu()

        try: 
            option = int(input("\nDigite a opção que deseja: "))
        except ValueError:
            print("Digite um número válido.")
            continue
        match option:
            case 1:
                add_tasks(tasks)
            case 2:
                list_tasks(tasks)
            case 3:
                remove_tasks(tasks)
            case 4:
                print("Saindo do sistema.")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

    '''''
while True:
    try:
        option = int(input("\nDigite uma das opções:\n1-Adicionar\n2-Listar\n3-Remover\n4-Sair\n"))
    except ValueError:
        print("\nPor favor, digite um número válido.")
        continue

    if (option == 4):
        print("Saindo do sistema.")
        break

    elif (option == 1):
        task = input("\nAdicione a tarefa: ")
        list_tasks.append(task)
        print("\nTarefa adicionada com sucesso.")

    elif (option == 2):
        if list_tasks:
            print("As tarefas são:")
            for i, num_task in enumerate(list_tasks, 1):
                print(f"{i}.{num_task}")
        else:
            print("\nNenhuma tarefa cadastrada.")

    elif (option == 3):
        if list_tasks:
            try:
                for i, task in enumerate(list_tasks, 1):
                    print(f"{i}.{task}")
                num_task = int(input("Digite o número da tarefa que deseja excluir: "))
                if 1 <= num_task <= len(list_tasks):
                    list_tasks.pop(num_task - 1)
                    print("Tarefa excluída com sucesso.")
                else:
                    print("\nNúmero inválido.")
            except ValueError:
                print("\nDigite um núemro válido.")
        else:
            print("\nA lista está vazia, não há tarefas para remover.")            
    else:
        print("Opção inválida>")
'''''