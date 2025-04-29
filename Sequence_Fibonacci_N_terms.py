num = int(input("Digite quantos termos da sequência Fibonacci você quer? "))
a, b = 0, 1
for _ in range(num):
    print(a, end=' ')
    a, b = b, a + b