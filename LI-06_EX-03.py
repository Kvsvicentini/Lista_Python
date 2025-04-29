#Solicitar dois números 
x = int(input("Digite um núemro: "))
y = int(input("Digite um número: "))

#Comparar os números lidos

if (x < y):
    for n in range(x + 1, y):
        print(n)
elif (x < y):
    for n in range(y + 1, x):
        print(n)
else:
    print("Os números são inválidos pois não há números entre eles")