x = float(input("Escolha algum dos nossos serviços: \n1-Realizar cadastro \n2-Recadastrar \n3-Sair \n"))
if(x == 1):
    nome = input("Digite o nome do cadastro: ")
    cpf = float(input("Digite seu CPF: "))
    rg = int(input('Digite seu RG: '))
    print("Cadastro concluído")
elif(x == 2):
    nome = input("Digite o nome do novo cadastro: ")
    cpf = float(input("Digite seu CPF: "))
    rg = int(input('Digite seu RG: '))
    print("Recadastro com sucesso")
else:
    print("Saindo do sistema")