grava = int(input("Digite um número: "))

y = 0

for i in range(1, 12):
    a = grava * y
    print(a)
    y += 1

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Agora vamos ler dois números e mostrar os números entres")
grava = int(input("Digite um número: "))
grava2 = int(input("Digite outro número: "))
if grava < grava2:
    for i in range (grava + 1, grava2):
        print(i)
elif grava > grava2:
    for i in range(grava2 + 1, grava):
        print(i)
else:
    print("Os números são iguais")