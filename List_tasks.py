list_tasks = []
print("\nVamos criar uma lista de tarefas.")

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