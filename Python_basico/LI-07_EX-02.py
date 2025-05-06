grava = int(input("Digite a sua idade: "))
if grava <= 10:
    print("Categoria: Infantil")
elif grava >= 11 and grava <= 14:
    print("Categoria: Infanto-juvenil")
elif grava >= 15 and grava <=17:
    print("Categoria: Juvenil")
else:
    print("Categoria: Adulto")