print("Vamos ler três números e mostrar os números entre os dois maiores")
num_1= int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))
list = [num_1, num_2, num_3]
list.sort(reverse=True)
list.pop()
maior_1 = max(list)
maior_2 = min(list)
if maior_1 < maior_2:
    for i in range( maior_1 + 1, maior_2):
        print(i)
    print("Estes são os números entre eles: ")
elif maior_1 > maior_2:
    for i in range(maior_2 + 1, maior_1):
        print(i)
    print("Estes são os números entre eles: ")
else:
    print("Os números digitados são iguais")